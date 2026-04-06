from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit, least_squares
from scipy.signal import find_peaks, savgol_filter


PLOT_FORMAT = "pdf"


def damped_cosine(t, amplitude, t2_ns, frequency_per_ns, phase_rad, offset):
    return offset + amplitude * np.exp(-t / t2_ns) * np.cos(2 * np.pi * frequency_per_ns * t + phase_rad)


def nodamp_cosine(t, amplitude, frequency_per_ns, phase_rad, offset):
    return offset + amplitude * np.cos(2 * np.pi * frequency_per_ns * t + phase_rad)


def trend_cosine(t, amplitude, frequency_per_ns, phase_rad, offset, slope):
    t0 = t - np.mean(t)
    return offset + slope * t0 + amplitude * np.cos(2 * np.pi * frequency_per_ns * t + phase_rad)


def safe_r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot <= 0:
        return np.nan
    return 1.0 - ss_res / ss_tot


def rmse(y_true, y_pred):
    return float(np.sqrt(np.mean((y_true - y_pred) ** 2)))


def odd_window_size(n_points, fraction=0.15, minimum=7, maximum=41):
    if n_points < minimum:
        size = max(3, n_points if n_points % 2 == 1 else n_points - 1)
        return size
    size = int(np.clip(n_points * fraction, minimum, maximum))
    if size % 2 == 0:
        size += 1
    if size >= n_points:
        size = n_points - 1 if n_points % 2 == 0 else n_points
    if size < 3:
        size = 3
    if size % 2 == 0:
        size += 1
    return size


def estimate_frequency_fft(t, y):
    if len(t) < 4:
        return 1e-4
    dt = float(np.mean(np.diff(t)))
    centered = y - np.mean(y)
    fft = np.fft.rfft(centered)
    freqs = np.fft.rfftfreq(len(centered), d=dt)
    if len(freqs) <= 1:
        return 1e-4
    idx = np.argmax(np.abs(fft[1:])) + 1
    return max(float(freqs[idx]), 1e-6)


def method_unconstrained_curve_fit(t, y, yerr, bounds_context):
    f0 = estimate_frequency_fft(t, y)
    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(max((np.max(t) - np.min(t)) / 2.0, 100.0)),
        float(f0),
        0.0,
        float(np.mean(y)),
    ]
    bounds = (
        [-np.inf, 1.0, 1e-8, -2 * np.pi, -np.inf],
        [np.inf, np.inf, 1.0, 2 * np.pi, np.inf],
    )
    popt, _ = curve_fit(damped_cosine, t, y, p0=p0, bounds=bounds, maxfev=25000)
    yfit = damped_cosine(t, *popt)
    return popt, yfit, "unconstrained"


def method_constrained_weighted(t, y, yerr, bounds_context):
    span = bounds_context["span"]
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]
    f0 = np.clip(estimate_frequency_fft(t, y), min_f, max_f)
    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(max(span, 100.0)),
        float(f0),
        0.0,
        float(np.mean(y)),
    ]
    bounds = (
        [-5 * np.ptp(y), span * 0.15, min_f, -2 * np.pi, np.min(y) - np.ptp(y)],
        [5 * np.ptp(y), span * 30.0, max_f, 2 * np.pi, np.max(y) + np.ptp(y)],
    )
    sigma = None
    if yerr is not None and np.all(yerr > 0):
        sigma = yerr
    popt, _ = curve_fit(
        damped_cosine,
        t,
        y,
        p0=p0,
        sigma=sigma,
        absolute_sigma=False,
        bounds=bounds,
        maxfev=30000,
    )
    yfit = damped_cosine(t, *popt)
    return popt, yfit, "weighted+constrained"


def method_robust_softl1(t, y, yerr, bounds_context):
    span = bounds_context["span"]
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]
    f0 = np.clip(estimate_frequency_fft(t, y), min_f, max_f)

    x0 = np.array(
        [
            float((np.max(y) - np.min(y)) / 2.0),
            float(max(span, 100.0)),
            float(f0),
            0.0,
            float(np.mean(y)),
        ]
    )
    lb = np.array([-5 * np.ptp(y), span * 0.15, min_f, -2 * np.pi, np.min(y) - np.ptp(y)])
    ub = np.array([5 * np.ptp(y), span * 30.0, max_f, 2 * np.pi, np.max(y) + np.ptp(y)])

    def residuals(par):
        pred = damped_cosine(t, *par)
        if yerr is not None and np.all(yerr > 0):
            return (pred - y) / yerr
        return pred - y

    result = least_squares(residuals, x0=x0, bounds=(lb, ub), loss="soft_l1", f_scale=0.75, max_nfev=40000)
    popt = result.x
    yfit = damped_cosine(t, *popt)
    return popt, yfit, "robust-soft_l1"


def method_nodamp_constrained(t, y, yerr, bounds_context):
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]
    f0 = np.clip(estimate_frequency_fft(t, y), min_f, max_f)
    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(f0),
        0.0,
        float(np.mean(y)),
    ]
    bounds = (
        [-5 * np.ptp(y), min_f, -2 * np.pi, np.min(y) - np.ptp(y)],
        [5 * np.ptp(y), max_f, 2 * np.pi, np.max(y) + np.ptp(y)],
    )
    popt, _ = curve_fit(nodamp_cosine, t, y, p0=p0, bounds=bounds, maxfev=30000)
    yfit = nodamp_cosine(t, *popt)
    popt_padded = [popt[0], np.inf, popt[1], popt[2], popt[3]]
    return popt_padded, yfit, "no-damping"


def method_trend_cosine(t, y, yerr, bounds_context):
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]
    f0 = np.clip(estimate_frequency_fft(t, y), min_f, max_f)
    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(f0),
        0.0,
        float(np.mean(y)),
        0.0,
    ]
    bounds = (
        [-5 * np.ptp(y), min_f, -2 * np.pi, np.min(y) - np.ptp(y), -5 * np.ptp(y) / max(bounds_context["span"], 1.0)],
        [5 * np.ptp(y), max_f, 2 * np.pi, np.max(y) + np.ptp(y), 5 * np.ptp(y) / max(bounds_context["span"], 1.0)],
    )
    popt, _ = curve_fit(trend_cosine, t, y, p0=p0, bounds=bounds, maxfev=30000)
    yfit = trend_cosine(t, *popt)
    popt_padded = [popt[0], np.inf, popt[1], popt[2], popt[3]]
    return popt_padded, yfit, f"trend-cosine (slope={popt[4]:.3e})"


def method_grid_frequency(t, y, yerr, bounds_context):
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]
    if max_f <= min_f:
        max_f = min_f * 1.2

    w = odd_window_size(len(y), fraction=0.18, minimum=7, maximum=41)
    trend = savgol_filter(y, window_length=w, polyorder=2, mode="interp")
    y_detr = y - trend

    f_grid = np.linspace(min_f, max_f, 1200)
    best = None
    best_rss = np.inf

    for f in f_grid:
        omega = 2 * np.pi * f * t
        X = np.column_stack([np.cos(omega), np.sin(omega), np.ones_like(t)])
        coef, *_ = np.linalg.lstsq(X, y_detr, rcond=None)
        pred = X @ coef
        rss = np.sum((y_detr - pred) ** 2)
        if rss < best_rss:
            best_rss = rss
            best = (f, coef)

    f_best, coef = best
    a_cos, b_sin, c0 = coef
    amplitude = float(np.sqrt(a_cos**2 + b_sin**2))
    phase = float(np.arctan2(-b_sin, a_cos))
    offset = float(np.mean(y - y_detr + c0))

    popt = np.array([amplitude, np.inf, f_best, phase, offset], dtype=float)
    yfit = nodamp_cosine(t, amplitude, f_best, phase, offset)
    return popt, yfit, "grid-frequency"


def method_multistart_damped(t, y, yerr, bounds_context, n_starts=40, seed=7):
    rng = np.random.default_rng(seed)
    span = bounds_context["span"]
    min_f = bounds_context["min_f"]
    max_f = bounds_context["max_f"]

    lb = np.array([-5 * np.ptp(y), span * 0.15, min_f, -2 * np.pi, np.min(y) - np.ptp(y)])
    ub = np.array([5 * np.ptp(y), span * 30.0, max_f, 2 * np.pi, np.max(y) + np.ptp(y)])

    def residuals(par):
        pred = damped_cosine(t, *par)
        if yerr is not None and np.all(yerr > 0):
            return (pred - y) / yerr
        return pred - y

    best = None
    best_cost = np.inf

    for _ in range(n_starts):
        x0 = np.array(
            [
                rng.uniform(lb[0], ub[0]),
                rng.uniform(lb[1], ub[1]),
                rng.uniform(lb[2], ub[2]),
                rng.uniform(lb[3], ub[3]),
                rng.uniform(lb[4], ub[4]),
            ]
        )
        res = least_squares(residuals, x0=x0, bounds=(lb, ub), max_nfev=10000)
        if res.cost < best_cost:
            best_cost = res.cost
            best = res.x

    popt = best
    yfit = damped_cosine(t, *popt)
    return popt, yfit, f"multi-start ({n_starts})"


def method_peak_seeded(t, y, yerr, bounds_context):
    w = odd_window_size(len(y), fraction=0.18, minimum=7, maximum=41)
    ys = savgol_filter(y, window_length=w, polyorder=2, mode="interp")

    peaks, _ = find_peaks(ys, distance=max(2, int(0.08 * len(y))))
    troughs, _ = find_peaks(-ys, distance=max(2, int(0.08 * len(y))))
    extrema = np.sort(np.concatenate([peaks, troughs]))
    if len(extrema) < 3:
        raise RuntimeError("Not enough extrema for peak-seeded estimate")

    half_period_est = float(np.median(np.diff(t[extrema])))
    if half_period_est <= 0:
        raise RuntimeError("Invalid peak-seeded half-period estimate")

    f_est = np.clip(1.0 / (2.0 * half_period_est), bounds_context["min_f"], bounds_context["max_f"])
    span = bounds_context["span"]

    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(max(span, 100.0)),
        float(f_est),
        0.0,
        float(np.mean(y)),
    ]
    bw_low = max(bounds_context["min_f"], 0.6 * f_est)
    bw_high = min(bounds_context["max_f"], 1.4 * f_est)
    bounds = (
        [-5 * np.ptp(y), span * 0.15, bw_low, -2 * np.pi, np.min(y) - np.ptp(y)],
        [5 * np.ptp(y), span * 30.0, bw_high, 2 * np.pi, np.max(y) + np.ptp(y)],
    )
    popt, _ = curve_fit(damped_cosine, t, y, p0=p0, bounds=bounds, maxfev=30000)
    yfit = damped_cosine(t, *popt)
    return popt, yfit, "peak-seeded"


METHODS = [
    ("unconstrained_damped", method_unconstrained_curve_fit),
    ("constrained_weighted", method_constrained_weighted),
    ("robust_softl1", method_robust_softl1),
    ("nodamp_constrained", method_nodamp_constrained),
    ("trend_cosine", method_trend_cosine),
    ("grid_frequency", method_grid_frequency),
    ("multistart_damped", method_multistart_damped),
    ("peak_seeded", method_peak_seeded),
]


def forced_period_fit_single_plot(results_dir, out_dir, target_file="Rabi_tau1.csv", t_min_ns=80.0, t_max_ns=150.0):
    csv_path = results_dir / target_file
    if not csv_path.exists():
        return None

    df = pd.read_csv(csv_path)
    if not {"tau_ns", "R_V"}.issubset(df.columns):
        return None

    t = df["tau_ns"].to_numpy(dtype=float)
    y = df["R_V"].to_numpy(dtype=float)
    yerr = df["Rstd"].to_numpy(dtype=float) if "Rstd" in df.columns else None

    idx = np.argsort(t)
    t = t[idx]
    y = y[idx]
    if yerr is not None:
        yerr = yerr[idx]

    span = float(np.max(t) - np.min(t))
    min_f = 1.0 / t_max_ns
    max_f = 1.0 / t_min_ns
    f0 = np.clip(estimate_frequency_fft(t, y), min_f, max_f)

    p0 = [
        float((np.max(y) - np.min(y)) / 2.0),
        float(max(span, 100.0)),
        float(f0),
        0.0,
        float(np.mean(y)),
    ]
    bounds = (
        [-5 * np.ptp(y), span * 0.15, min_f, -2 * np.pi, np.min(y) - np.ptp(y)],
        [5 * np.ptp(y), span * 30.0, max_f, 2 * np.pi, np.max(y) + np.ptp(y)],
    )

    sigma = None
    if yerr is not None and np.all(yerr > 0):
        sigma = yerr

    popt, _ = curve_fit(
        damped_cosine,
        t,
        y,
        p0=p0,
        sigma=sigma,
        absolute_sigma=False,
        bounds=bounds,
        maxfev=40000,
    )
    yfit = damped_cosine(t, *popt)
    r2_value = safe_r2(y, yfit)
    period = 1.0 / popt[2]
    cycles = span * popt[2]

    text = (
        "Forced period fit\n"
        + f"Constraint: 80 ns ≤ T ≤ 150 ns\n"
        + r"$R(\tau)=C + A e^{-\tau/T_2^*}\cos(2\pi f\tau+\phi)$"
        + "\n"
        + f"A={popt[0]*1e3:.3f} mV\n"
        + f"T2*={popt[1]:.2f} ns\n"
        + f"f={popt[2]:.5f} 1/ns\n"
        + f"T={period:.2f} ns\n"
        + f"cycles in window={cycles:.2f}\n"
        + f"R²={r2_value:.4f}"
    )

    plot_base = out_dir / "Rabi_tau1__forced_period_80_150ns"
    make_single_plot(
        t=t,
        y=y,
        yerr=yerr,
        yfit=yfit,
        title="Rabi forced-period fit (Rabi_tau1.csv)",
        text=text,
        out_path=plot_base,
    )

    forced_row = {
        "file": target_file,
        "method": "forced_period_80_150ns",
        "note": "frequency constrained by 80<=T<=150 ns",
        "r2": float(r2_value),
        "rmse_V": rmse(y, yfit),
        "amplitude_V": float(popt[0]),
        "t2star_ns": float(popt[1]),
        "frequency_per_ns": float(popt[2]),
        "period_ns": float(period),
        "cycles_in_window": float(cycles),
        "offset_V": float(popt[4]),
        "phase_rad": float(popt[3]),
        "score": score_method(float(r2_value), float(cycles)),
        "plot": plot_base.with_suffix(f".{PLOT_FORMAT}").name,
    }
    return forced_row


def score_method(r2_value, cycles):
    if np.isnan(r2_value):
        return -np.inf
    cycle_bonus = min(cycles, 3.0) * 0.08
    cycle_penalty = 0.25 if cycles < 0.6 else 0.0
    return float(r2_value + cycle_bonus - cycle_penalty)


def make_single_plot(t, y, yerr, yfit, title, text, out_path):
    fig, ax = plt.subplots(figsize=(10, 5), dpi=140)
    if yerr is not None and np.any(yerr > 0):
        ax.errorbar(t, y * 1e3, yerr=yerr * 1e3, fmt="o", markersize=3, alpha=0.9, label="Data")
    else:
        ax.plot(t, y * 1e3, "o", markersize=3, alpha=0.9, label="Data")
    ax.plot(t, yfit * 1e3, "-", linewidth=2.0, label="Fit")
    ax.set_xlabel("MW pulse length τ (ns)")
    ax.set_ylabel("Lock-in R (mV)")
    ax.set_title(title)
    ax.grid(True, ls=":", alpha=0.6)
    ax.legend(loc="upper right")
    ax.text(
        0.01,
        0.99,
        text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        fontsize=9,
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
    )
    fig.tight_layout()
    fig.savefig(out_path.with_suffix(f".{PLOT_FORMAT}"), bbox_inches="tight")
    plt.close(fig)


def make_overlay_plot(t, y, yerr, fit_rows, out_path, title):
    fig, ax = plt.subplots(figsize=(11, 6), dpi=140)
    if yerr is not None and np.any(yerr > 0):
        ax.errorbar(t, y * 1e3, yerr=yerr * 1e3, fmt="o", color="black", markersize=3, alpha=0.8, label="Data")
    else:
        ax.plot(t, y * 1e3, "o", color="black", markersize=3, alpha=0.8, label="Data")

    palette = plt.cm.tab10(np.linspace(0, 1, max(3, len(fit_rows))))
    for i, row in enumerate(fit_rows):
        ax.plot(t, row["yfit"] * 1e3, "-", lw=1.6, color=palette[i % len(palette)], label=f"{row['method']} (R²={row['r2']:.3f})")

    ax.set_xlabel("MW pulse length τ (ns)")
    ax.set_ylabel("Lock-in R (mV)")
    ax.set_title(title)
    ax.grid(True, ls=":", alpha=0.6)
    ax.legend(fontsize=8, ncol=2)
    fig.tight_layout()
    fig.savefig(out_path.with_suffix(f".{PLOT_FORMAT}"), bbox_inches="tight")
    plt.close(fig)


def run_for_rabi_file(csv_path, out_dir):
    df = pd.read_csv(csv_path)
    if not {"tau_ns", "R_V"}.issubset(df.columns):
        raise ValueError(f"Missing required columns in {csv_path.name}")

    t = df["tau_ns"].to_numpy(dtype=float)
    y = df["R_V"].to_numpy(dtype=float)
    yerr = df["Rstd"].to_numpy(dtype=float) if "Rstd" in df.columns else None

    idx = np.argsort(t)
    t = t[idx]
    y = y[idx]
    if yerr is not None:
        yerr = yerr[idx]

    span = float(np.max(t) - np.min(t))
    dt = float(np.mean(np.diff(t))) if len(t) > 1 else 1.0
    nyquist = 0.5 / dt
    min_f = max(0.5 / max(span, 1.0), 1e-6)
    max_f = max(min(0.90 * nyquist, 0.04), min_f * 1.5)
    context = {"span": span, "min_f": min_f, "max_f": max_f}

    method_rows = []

    for method_name, method_fn in METHODS:
        try:
            popt, yfit, note = method_fn(t, y, yerr, context)
            r2_value = float(safe_r2(y, yfit))
            rmse_value = rmse(y, yfit)
            f = float(popt[2])
            period = float(np.inf if f <= 0 else 1.0 / f)
            cycles = float(span * f)
            score = score_method(r2_value, cycles)

            info_text = (
                f"Method: {method_name}\n"
                + f"Note: {note}\n"
                + r"$R(\tau)=C + A e^{-\tau/T_2^*}\cos(2\pi f\tau+\phi)$"
                + "\n"
                + f"A={popt[0]*1e3:.3f} mV\n"
                + f"T2*={popt[1]:.2f} ns\n"
                + f"f={f:.4e} 1/ns\n"
                + f"Period={period:.1f} ns\n"
                + f"Cycles in window={cycles:.3f}\n"
                + f"R²={r2_value:.4f}, RMSE={rmse_value*1e3:.4f} mV"
            )

            single_plot_base = out_dir / f"{csv_path.stem}__{method_name}"
            make_single_plot(
                t=t,
                y=y,
                yerr=yerr,
                yfit=yfit,
                title=f"Rabi Fit Improvement: {csv_path.stem} ({method_name})",
                text=info_text,
                out_path=single_plot_base,
            )

            method_rows.append(
                {
                    "file": csv_path.name,
                    "method": method_name,
                    "note": note,
                    "r2": r2_value,
                    "rmse_V": rmse_value,
                    "amplitude_V": float(popt[0]),
                    "t2star_ns": float(popt[1]),
                    "frequency_per_ns": f,
                    "period_ns": period,
                    "cycles_in_window": cycles,
                    "offset_V": float(popt[4]),
                    "phase_rad": float(popt[3]),
                    "score": score,
                    "plot": single_plot_base.with_suffix(f".{PLOT_FORMAT}").name,
                    "yfit": yfit,
                }
            )

        except Exception as exc:
            method_rows.append(
                {
                    "file": csv_path.name,
                    "method": method_name,
                    "note": f"FAILED: {exc}",
                    "r2": np.nan,
                    "rmse_V": np.nan,
                    "amplitude_V": np.nan,
                    "t2star_ns": np.nan,
                    "frequency_per_ns": np.nan,
                    "period_ns": np.nan,
                    "cycles_in_window": np.nan,
                    "offset_V": np.nan,
                    "phase_rad": np.nan,
                    "score": -np.inf,
                    "plot": "",
                    "yfit": None,
                }
            )

    successful = [row for row in method_rows if row["yfit"] is not None]
    if successful:
        successful_sorted = sorted(successful, key=lambda x: x["score"], reverse=True)
        make_overlay_plot(
            t=t,
            y=y,
            yerr=yerr,
            fit_rows=successful_sorted,
            out_path=out_dir / f"{csv_path.stem}__overlay_all_methods",
            title=f"Rabi Method Comparison: {csv_path.stem}",
        )

        best = successful_sorted[0]
        make_overlay_plot(
            t=t,
            y=y,
            yerr=yerr,
            fit_rows=successful_sorted[:3],
            out_path=out_dir / f"{csv_path.stem}__overlay_top3",
            title=(
                f"Rabi Top-3 Methods: {csv_path.stem} | "
                f"Best={best['method']} (R²={best['r2']:.3f}, cycles={best['cycles_in_window']:.2f})"
            ),
        )

    for row in method_rows:
        row.pop("yfit", None)
    return method_rows


def main():
    root = Path(__file__).resolve().parent
    results_dir = root / "results"
    out_dir = results_dir / "analysis" / "rabi_improvement"
    out_dir.mkdir(parents=True, exist_ok=True)

    rabi_files = sorted([p for p in results_dir.glob("Rabi*.csv") if p.is_file()])
    if not rabi_files:
        print("No Rabi CSV files found.")
        return

    all_rows = []
    for csv_path in rabi_files:
        rows = run_for_rabi_file(csv_path, out_dir)
        all_rows.extend(rows)
        print(f"Processed {csv_path.name} with {len(rows)} methods")

    forced = forced_period_fit_single_plot(results_dir, out_dir)
    if forced is not None:
        all_rows.append(forced)
        print(f"Generated forced-period plot: {forced['plot']}")

    summary_df = pd.DataFrame(all_rows)
    summary_path = out_dir / "rabi_methods_summary.csv"
    summary_df.to_csv(summary_path, index=False)

    ranked_df = summary_df.sort_values(["file", "score"], ascending=[True, False]).copy()
    ranked_path = out_dir / "rabi_methods_ranked.csv"
    ranked_df.to_csv(ranked_path, index=False)

    best_rows = ranked_df.groupby("file", as_index=False).first()
    best_path = out_dir / "rabi_best_per_file.csv"
    best_rows.to_csv(best_path, index=False)

    print("\n=== Rabi Fit Improvement Complete ===")
    print(f"Output directory: {out_dir}")
    print(f"Methods summary: {summary_path}")
    print(f"Methods ranked: {ranked_path}")
    print(f"Best per file: {best_path}")


if __name__ == "__main__":
    main()
