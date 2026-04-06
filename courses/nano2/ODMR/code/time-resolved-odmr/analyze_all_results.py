import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.optimize import curve_fit
from scipy.signal import find_peaks, savgol_filter


# ----------------------------
# User-editable plotting setup
# ----------------------------
PLOT_FORMAT = "pdf"

# CW resonance detection behavior
SHOW_CW_RESONANCE_MARKERS = True
CW_FIND_MAXIMA = True
CW_PROMINENCE_FRACTION = 0.12
CW_PROMINENCE_SIGMA = 1.0
CW_MIN_DISTANCE_FRACTION = 0.06
CW_MAX_RESONANCES = 8

# Notebook result files we expect to cover in analysis
EXPECTED_NOTEBOOK_RESULT_FILES = [
    "CW_Sweep.csv",
    "CW_SweepREDO.csv",
    "CW_Sweep_magnet.csv",
    "CW_Sweep_magnet2.csv",
    "CW_Sweep_magnetFOCUS.csv",
    "CW_Sweep_magnetREDO.csv",
    "CW_Sweep_magnetREDO2.csv",
    "Rabi_Corrected.csv",
    "Rabi_tau1.csv",
    "T1_Sweep.csv",
    "T1_Sweep2.csv",
    "T1_relaxation.json",
]


def t1_model(tau_ns, amplitude, t1_ns, offset):
    return amplitude * np.exp(-tau_ns / t1_ns) + offset


def rabi_model(tau_ns, amplitude, t2star_ns, frequency_per_ns, phase_rad, offset):
    return (
        offset
        + amplitude
        * np.exp(-tau_ns / t2star_ns)
        * np.cos(2 * np.pi * frequency_per_ns * tau_ns + phase_rad)
    )


def safe_r2(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    if ss_tot == 0:
        return np.nan
    return 1 - ss_res / ss_tot


def ensure_dir(path):
    path.mkdir(parents=True, exist_ok=True)


def save_figure(fig, path_without_extension):
    out_path = path_without_extension.with_suffix(f".{PLOT_FORMAT}")
    fig.savefig(out_path, bbox_inches="tight")
    plt.close(fig)
    return out_path


def odd_window_size(n_points, fraction=0.15, min_size=7, max_size=51):
    if n_points < min_size:
        return max(3, n_points if n_points % 2 == 1 else n_points - 1)
    size = int(max(min_size, min(max_size, n_points * fraction)))
    if size % 2 == 0:
        size += 1
    if size >= n_points:
        size = n_points - 1 if n_points % 2 == 0 else n_points
    if size < 3:
        size = 3
    if size % 2 == 0:
        size += 1
    return size


def convert_t1_json_lossless(json_path, out_dir):
    with open(json_path, "r", encoding="utf-8") as f:
        raw = json.load(f)

    measurement_ids = sorted([int(k) for k in raw["Tau"].keys()])
    measurement_keys = [str(k) for k in measurement_ids]

    scalar_columns = [k for k in raw.keys() if k != "Rs"]
    scalar_df = pd.DataFrame({
        "measurement_index": measurement_ids,
        **{
            col: [raw[col][k] for k in measurement_keys]
            for col in scalar_columns
        },
    })

    rs_lists = [raw["Rs"][k] for k in measurement_keys]
    rs_max_len = max(len(v) for v in rs_lists)

    rs_wide_df = pd.DataFrame(
        {
            "measurement_index": measurement_ids,
            **{
                f"Rs_{i:03d}": [vals[i] if i < len(vals) else np.nan for vals in rs_lists]
                for i in range(rs_max_len)
            },
        }
    )

    long_rows = []
    for measurement_index, vals in zip(measurement_ids, rs_lists):
        for sample_index, value in enumerate(vals):
            long_rows.append(
                {
                    "measurement_index": measurement_index,
                    "sample_index": sample_index,
                    "Rs_V": value,
                }
            )
    rs_long_df = pd.DataFrame(long_rows)

    scalar_path = out_dir / "T1_relaxation_scalar.csv"
    rs_wide_path = out_dir / "T1_relaxation_Rs_wide.csv"
    rs_long_path = out_dir / "T1_relaxation_Rs_long.csv"

    scalar_df.to_csv(scalar_path, index=False)
    rs_wide_df.to_csv(rs_wide_path, index=False)
    rs_long_df.to_csv(rs_long_path, index=False)

    analysis_ready_df = scalar_df.rename(columns={"Tau": "tau_ns", "Rmean": "R_V", "Rstd": "Rstd"})
    analysis_ready_path = out_dir / "T1_relaxation_for_fit.csv"
    analysis_ready_df.to_csv(analysis_ready_path, index=False)

    return {
        "scalar_path": scalar_path,
        "rs_wide_path": rs_wide_path,
        "rs_long_path": rs_long_path,
        "analysis_ready_path": analysis_ready_path,
        "rows": len(scalar_df),
        "samples_per_row": rs_max_len,
    }


def analyze_cw_file(csv_path, plot_dir):
    df = pd.read_csv(csv_path)
    if not {"freq_GHz", "R_V"}.issubset(df.columns):
        raise ValueError(f"Missing required columns in {csv_path.name}")

    x = df["freq_GHz"].to_numpy(dtype=float)
    y = df["R_V"].to_numpy(dtype=float)

    w = odd_window_size(len(y), fraction=0.16, min_size=7, max_size=41)
    y_smooth = savgol_filter(y, window_length=w, polyorder=2, mode="interp")

    y_range = float(np.max(y_smooth) - np.min(y_smooth))
    prominence = max(
        y_range * CW_PROMINENCE_FRACTION,
        float(np.std(y_smooth)) * CW_PROMINENCE_SIGMA,
        1e-12,
    )
    distance = max(1, int(len(y) * CW_MIN_DISTANCE_FRACTION))

    if CW_FIND_MAXIMA:
        resonance_idx, props = find_peaks(y_smooth, prominence=prominence, distance=distance)
    else:
        resonance_idx, props = find_peaks(-y_smooth, prominence=prominence, distance=distance)

    if len(resonance_idx) > CW_MAX_RESONANCES:
        strongest = np.argsort(props["prominences"])[-CW_MAX_RESONANCES:]
        resonance_idx = resonance_idx[strongest]
    resonance_idx = np.array(sorted(resonance_idx.tolist()), dtype=int)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
    ax.plot(x, y, "o", markersize=3, alpha=0.6, label="Raw data")
    ax.plot(x, y_smooth, "-", linewidth=2, label="Smoothed trace")

    if SHOW_CW_RESONANCE_MARKERS and len(resonance_idx) > 0:
        marker = "^" if CW_FIND_MAXIMA else "v"
        ax.plot(
            x[resonance_idx],
            y_smooth[resonance_idx],
            marker,
            color="crimson",
            markersize=7,
            linestyle="None",
            label="Detected resonances",
        )
        for idx in resonance_idx:
            ax.annotate(
                f"{x[idx]:.4f} GHz",
                xy=(x[idx], y_smooth[idx]),
                xytext=(0, 8),
                textcoords="offset points",
                ha="center",
                fontsize=8,
                rotation=90,
            )

    extrema_text = "Maxima" if CW_FIND_MAXIMA else "Minima"
    ax.text(
        0.01,
        0.99,
        f"Detection: {extrema_text}\nProminence >= {prominence:.3e} V\nMin distance: {distance} points",
        transform=ax.transAxes,
        va="top",
        ha="left",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
        fontsize=9,
    )

    ax.set_xlabel("Frequency (GHz)")
    ax.set_ylabel("Lock-in R (V)")
    ax.set_title(f"CW Analysis: {csv_path.stem}")
    ax.grid(True, ls=":", alpha=0.6)
    ax.legend()
    fig.tight_layout()
    out_plot = save_figure(fig, plot_dir / f"{csv_path.stem}_analysis")

    resonances = ";".join([f"{x[i]:.6f}" for i in resonance_idx]) if len(resonance_idx) else ""
    return {
        "file": csv_path.name,
        "type": "CW",
        "n_points": len(df),
        "freq_min_GHz": float(np.min(x)),
        "freq_max_GHz": float(np.max(x)),
        "signal_min_V": float(np.min(y)),
        "signal_max_V": float(np.max(y)),
        "global_max_freq_GHz": float(x[np.argmax(y)]),
        "global_min_freq_GHz": float(x[np.argmin(y)]),
        "n_detected_resonances": int(len(resonance_idx)),
        "detected_resonance_freqs_GHz": resonances,
        "detection_mode": "maxima" if CW_FIND_MAXIMA else "minima",
        "plot": out_plot.name,
    }


def analyze_rabi_file(csv_path, plot_dir):
    df = pd.read_csv(csv_path)
    if not {"tau_ns", "R_V"}.issubset(df.columns):
        raise ValueError(f"Missing required columns in {csv_path.name}")

    t = df["tau_ns"].to_numpy(dtype=float)
    y = df["R_V"].to_numpy(dtype=float)
    yerr = df["Rstd"].to_numpy(dtype=float) if "Rstd" in df.columns else None

    sort_idx = np.argsort(t)
    t = t[sort_idx]
    y = y[sort_idx]
    if yerr is not None:
        yerr = yerr[sort_idx]

    dt = np.mean(np.diff(t)) if len(t) > 1 else 1.0
    centered = y - np.mean(y)
    fft = np.fft.rfft(centered)
    freqs = np.fft.rfftfreq(len(centered), d=dt)
    if len(freqs) > 1:
        dominant = np.argmax(np.abs(fft[1:])) + 1
        f0 = max(freqs[dominant], 1e-6)
    else:
        f0 = 1e-4

    p0 = [
        (np.max(y) - np.min(y)) / 2,
        max((np.max(t) - np.min(t)) / 2, 100),
        f0,
        0.0,
        np.mean(y),
    ]

    bounds = (
        [-np.inf, 1.0, 1e-8, -2 * np.pi, -np.inf],
        [np.inf, np.inf, 1.0, 2 * np.pi, np.inf],
    )

    popt, _ = curve_fit(rabi_model, t, y, p0=p0, bounds=bounds, maxfev=20000)
    y_fit = rabi_model(t, *popt)

    amplitude, t2star_ns, frequency_per_ns, phase_rad, offset = popt
    period_ns = 1.0 / frequency_per_ns
    pi_pulse_ns = period_ns / 2.0
    r2 = safe_r2(y, y_fit)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
    if yerr is not None:
        ax.errorbar(t, y * 1e3, yerr=yerr * 1e3, fmt="o", markersize=3, label="Data")
    else:
        ax.plot(t, y * 1e3, "o", markersize=3, label="Data")
    ax.plot(t, y_fit * 1e3, "-", lw=2, label="Damped cosine fit")

    model_text = (
        r"$R(\tau)=C + A e^{-\tau/T_2^*}\cos(2\pi f\tau+\phi)$"
        + "\n"
        + f"A = {amplitude*1e3:.3f} mV\n"
        + f"T2* = {t2star_ns:.1f} ns\n"
        + f"f = {frequency_per_ns:.4e} 1/ns\n"
        + f"Period = {period_ns:.1f} ns, π-pulse = {pi_pulse_ns:.1f} ns\n"
        + f"Offset = {offset*1e3:.3f} mV, Phase = {phase_rad:.3f} rad\n"
        + f"R² = {r2:.4f}"
    )
    ax.text(
        0.01,
        0.99,
        model_text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
        fontsize=9,
    )

    ax.set_xlabel("MW pulse length tau (ns)")
    ax.set_ylabel("Lock-in R (mV)")
    ax.set_title(f"Rabi Analysis: {csv_path.stem}")
    ax.grid(True, ls=":", alpha=0.6)
    ax.legend()
    fig.tight_layout()
    out_plot = save_figure(fig, plot_dir / f"{csv_path.stem}_analysis")

    return {
        "file": csv_path.name,
        "type": "Rabi",
        "n_points": len(df),
        "amplitude_V": float(amplitude),
        "t2star_ns": float(t2star_ns),
        "frequency_per_ns": float(frequency_per_ns),
        "period_ns": float(period_ns),
        "pi_pulse_ns": float(pi_pulse_ns),
        "offset_V": float(offset),
        "phase_rad": float(phase_rad),
        "r2": float(r2),
        "plot": out_plot.name,
    }


def analyze_t1_file(csv_path, plot_dir):
    df = pd.read_csv(csv_path)
    if not {"tau_ns", "R_V"}.issubset(df.columns):
        raise ValueError(f"Missing required columns in {csv_path.name}")

    t = df["tau_ns"].to_numpy(dtype=float)
    y = df["R_V"].to_numpy(dtype=float)
    yerr = df["Rstd"].to_numpy(dtype=float) if "Rstd" in df.columns else None

    sort_idx = np.argsort(t)
    t = t[sort_idx]
    y = y[sort_idx]
    if yerr is not None:
        yerr = yerr[sort_idx]

    p0 = [y[0] - y[-1], max((np.max(t) - np.min(t)) / 3, 1000), y[-1]]
    bounds = ([-np.inf, 1.0, -np.inf], [np.inf, np.inf, np.inf])
    popt, _ = curve_fit(t1_model, t, y, p0=p0, bounds=bounds, maxfev=20000)
    y_fit = t1_model(t, *popt)
    amplitude, t1_ns, offset = popt
    r2 = safe_r2(y, y_fit)

    fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
    if yerr is not None:
        ax.errorbar(t / 1e6, y * 1e3, yerr=yerr * 1e3, fmt="o", markersize=3, label="Data")
    else:
        ax.plot(t / 1e6, y * 1e3, "o", markersize=3, label="Data")
    ax.plot(t / 1e6, y_fit * 1e3, "-", lw=2, label="Exponential fit")

    model_text = (
        r"$R(\tau)=C + A e^{-\tau/T_1}$"
        + "\n"
        + f"A = {amplitude*1e3:.3f} mV\n"
        + f"T1 = {t1_ns:.1f} ns = {t1_ns/1e6:.6f} ms\n"
        + f"Offset C = {offset*1e3:.3f} mV\n"
        + f"R² = {r2:.4f}"
    )
    ax.text(
        0.01,
        0.99,
        model_text,
        transform=ax.transAxes,
        va="top",
        ha="left",
        bbox={"boxstyle": "round", "facecolor": "white", "alpha": 0.85},
        fontsize=9,
    )

    ax.set_xscale("log")
    ax.set_xlabel("Relaxation delay tau (ms)")
    ax.set_ylabel("Lock-in R (mV)")
    ax.set_title(f"T1 Analysis: {csv_path.stem}")
    ax.grid(True, which="both", ls=":", alpha=0.6)
    ax.legend()
    fig.tight_layout()
    out_plot = save_figure(fig, plot_dir / f"{csv_path.stem}_analysis")

    return {
        "file": csv_path.name,
        "type": "T1",
        "n_points": len(df),
        "amplitude_V": float(amplitude),
        "t1_ns": float(t1_ns),
        "t1_ms": float(t1_ns / 1e6),
        "offset_V": float(offset),
        "r2": float(r2),
        "plot": out_plot.name,
    }


def main():
    root = Path(__file__).resolve().parent
    results_dir = root / "results"
    analysis_dir = results_dir / "analysis"
    plots_dir = analysis_dir / "plots"
    converted_dir = analysis_dir / "converted"

    ensure_dir(analysis_dir)
    ensure_dir(plots_dir)
    ensure_dir(converted_dir)

    summary_rows = []
    conversion_rows = []
    coverage_rows = []

    json_path = results_dir / "T1_relaxation.json"
    generated_t1_csv = None
    if json_path.exists():
        conversion_info = convert_t1_json_lossless(json_path, converted_dir)
        conversion_rows.append(
            {
                "file": json_path.name,
                "type": "JSON_CONVERSION",
                "rows": conversion_info["rows"],
                "samples_per_row": conversion_info["samples_per_row"],
                "scalar_csv": conversion_info["scalar_path"].name,
                "rs_wide_csv": conversion_info["rs_wide_path"].name,
                "rs_long_csv": conversion_info["rs_long_path"].name,
                "fit_csv": conversion_info["analysis_ready_path"].name,
            }
        )
        generated_t1_csv = conversion_info["analysis_ready_path"]

    csv_files = sorted(results_dir.glob("*.csv"))

    existing_files = {p.name for p in results_dir.glob("*") if p.is_file()}
    for file_name in EXPECTED_NOTEBOOK_RESULT_FILES:
        coverage_rows.append(
            {
                "expected_file": file_name,
                "exists": file_name in existing_files,
            }
        )

    for csv_path in csv_files:
        if csv_path.name.startswith("CW"):
            result = analyze_cw_file(csv_path, plots_dir)
        elif csv_path.name.startswith("Rabi"):
            result = analyze_rabi_file(csv_path, plots_dir)
        elif csv_path.name.startswith("T1"):
            result = analyze_t1_file(csv_path, plots_dir)
        else:
            continue
        summary_rows.append(result)
        print(f"Processed {csv_path.name} ({result['type']})")

    if generated_t1_csv is not None:
        result = analyze_t1_file(generated_t1_csv, plots_dir)
        summary_rows.append(result)
        print(f"Processed {generated_t1_csv.name} (T1 from JSON)")

    summary_df = pd.DataFrame(summary_rows)
    conversion_df = pd.DataFrame(conversion_rows)
    coverage_df = pd.DataFrame(coverage_rows)

    summary_path = analysis_dir / "analysis_summary.csv"
    conversion_path = analysis_dir / "json_conversion_summary.csv"
    coverage_path = analysis_dir / "notebook_coverage.csv"
    summary_df.to_csv(summary_path, index=False)
    conversion_df.to_csv(conversion_path, index=False)
    coverage_df.to_csv(coverage_path, index=False)

    print("\n=== Analysis Complete ===")
    print(f"Summary table: {summary_path}")
    print(f"JSON conversion table: {conversion_path}")
    print(f"Notebook coverage: {coverage_path}")
    print(f"Plots: {plots_dir}")

    if not summary_df.empty:
        display_cols = [
            c
            for c in [
                "file",
                "type",
                "r2",
                "t1_ms",
                "pi_pulse_ns",
                "global_max_freq_GHz",
                "global_min_freq_GHz",
                "n_detected_resonances",
            ]
            if c in summary_df.columns
        ]
        print("\nKey results:")
        print(summary_df[display_cols].to_string(index=False))


if __name__ == "__main__":
    main()
