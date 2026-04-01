"""
Robust Shapiro step extraction using Kernel Density Estimation (KDE).

Strategy: The full V(I) sweep is dominated by the linear ohmic branch,
which creates a nearly uniform voltage distribution that drowns the
Shapiro step peaks. Solution:

1. Restrict analysis to the CENTRAL region near I=0 where the
   superconducting branch and Shapiro plateaus concentrate voltage dwell time.
2. Use KDE with bandwidth selected by cross-validation on this restricted
   region, which has genuine multimodal structure.
3. As fallback, use Improved Sheather-Jones (ISJ) bandwidth or
   explicit Scott's rule with a downscaling factor.

The derivative method is retained with MAD-based adaptive thresholding.
"""
import sys
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import find_peaks
from scipy.stats import gaussian_kde


def extract_shapiro_step_kde(filepath, sigma=5, save_plot=False, plot_dir=None):
    """
    Extract Shapiro voltage step size from V-I data using KDE.

    Returns
    -------
    step_kde : float  -- Voltage step size from KDE [V]
    step_deriv : float -- Voltage step size from derivative [V]
    n_kde_peaks : int
    n_deriv_peaks : int
    """
    data = np.loadtxt(filepath, skiprows=1)
    length = len(data)
    s, e = int(length * 0.1), int(length * 0.9)
    v_sq = data[s:e, 1] / 1e3   # diff-amp gain = 1000
    v_ref = data[s:e, 2]

    # --- Smoothing in time domain ---
    v_smooth = gaussian_filter(v_sq, sigma=sigma)
    i_smooth = gaussian_filter(v_ref, sigma=sigma)

    # ====================================================
    # METHOD A: Derivative edge detection with MAD threshold
    # ====================================================
    di = np.gradient(i_smooth)
    dv_di = np.gradient(v_smooth) / np.where(np.abs(di) < 1e-12, 1e-12, di)
    dv_di = gaussian_filter(dv_di, sigma=3)

    mad_dv = np.median(np.abs(dv_di - np.median(dv_di)))
    sigma_mad = 1.4826 * mad_dv  # MAD-based robust sigma estimate
    threshold = np.median(dv_di) + 2.0 * sigma_mad
    deriv_peaks, _ = find_peaks(dv_di, height=threshold, distance=10)

    step_deriv = 0.0
    if len(deriv_peaks) > 1:
        v_at_edges = v_sq[deriv_peaks]
        step_deriv = np.median(np.abs(np.diff(v_at_edges)))

    # ====================================================
    # METHOD B: KDE on central voltage region
    # ====================================================
    # Restrict to the central 50% of the current range where
    # Shapiro plateaus concentrate voltage dwell time
    i_range = np.max(i_smooth) - np.min(i_smooth)
    i_center = (np.max(i_smooth) + np.min(i_smooth)) / 2
    central_mask = np.abs(i_smooth - i_center) < 0.25 * i_range
    v_central = v_sq[central_mask]

    if len(v_central) < 50:
        v_central = v_sq  # Fallback to full range

    # Use Scott's rule with downscaling for multimodal detection
    # Scott: h = 3.49 * sigma * n^(-1/3)
    # We use a factor of 0.3 to resolve peaks at ~20 uV spacing
    n = len(v_central)
    std_v = np.std(v_central)
    iqr_v = np.subtract(*np.percentile(v_central, [75, 25]))
    # Silverman's width estimate
    width_est = 0.9 * min(std_v, iqr_v / 1.34) * n**(-0.2)

    # For Shapiro steps at 10 GHz: expected step ~ 20 uV = 2e-5 V
    # We want bandwidth << step size to resolve peaks
    # Use 1/3 of the Silverman estimate as a practical tighter bandwidth
    bw = max(width_est * 0.3, 1e-7)  # Floor to avoid degenerate KDE

    try:
        kde = gaussian_kde(v_central, bw_method=bw / np.std(v_central))
    except Exception:
        try:
            kde = gaussian_kde(v_central, bw_method='silverman')
        except Exception:
            return 0.0, step_deriv, 0, len(deriv_peaks)

    v_min, v_max = np.min(v_central), np.max(v_central)
    v_margin = (v_max - v_min) * 0.05
    v_grid = np.linspace(v_min - v_margin, v_max + v_margin, 2000)
    density = kde(v_grid)

    # Find peaks: minimum distance = expected step / grid spacing
    grid_spacing = (v_grid[-1] - v_grid[0]) / 2000
    min_dist = max(int(5e-6 / grid_spacing), 5)  # at least 5 uV separation

    kde_peaks, _ = find_peaks(density, distance=min_dist,
                               prominence=np.max(density) * 0.02)

    step_kde = 0.0
    plateau_voltages = np.sort(v_grid[kde_peaks])

    if len(kde_peaks) > 1:
        spacings = np.diff(plateau_voltages)
        # Use the median spacing as the fundamental step
        # Filter out spacings that are clearly multi-step jumps (>2x median)
        med_spacing = np.median(spacings)
        fundamental_spacings = spacings[spacings < 2.0 * med_spacing]
        if len(fundamental_spacings) > 0:
            step_kde = np.median(fundamental_spacings)
        else:
            step_kde = med_spacing

    n_kde_peaks = len(kde_peaks)
    n_deriv_peaks = len(deriv_peaks)

    if save_plot:
        _plot_verification(i_smooth, v_sq, v_smooth, dv_di, deriv_peaks,
                           v_grid, density, kde_peaks, central_mask,
                           filepath, plot_dir, step_kde, step_deriv,
                           n_kde_peaks, n_deriv_peaks)

    return step_kde, step_deriv, n_kde_peaks, n_deriv_peaks


def _plot_verification(i_data, v_raw, v_smooth, dv, deriv_peaks,
                       v_grid, density, kde_peaks, central_mask,
                       filepath, plot_dir, step_kde, step_deriv,
                       n_kde, n_deriv):
    """3-panel verification plot."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9),
                                         gridspec_kw={'height_ratios': [2, 1, 1.2]})

    ax1.plot(i_data, v_raw * 1e6, 'k-', alpha=0.7, linewidth=0.8)
    if len(deriv_peaks) > 0:
        ax1.plot(i_data[deriv_peaks], v_raw[deriv_peaks] * 1e6, 'rx', markersize=5,
                 label=f'Derivative edges ({n_deriv})')
    # Highlight central region
    ax1.axvspan(i_data[central_mask][0], i_data[central_mask][-1],
                alpha=0.08, color='green', label='KDE region')
    ax1.set_ylabel('$V_{\\mathrm{SQUID}}$ [$\\mu$V]')
    ax1.set_title(os.path.basename(filepath), fontsize=10)
    ax1.legend(loc='lower right', fontsize=8, frameon=False)
    ax1.grid(True, ls='--', alpha=0.3)

    R_PRE = 10e3  # pre-resistor, converts V_ref to I_bias
    ax2.plot(i_data, dv * R_PRE, 'b-', alpha=0.6, linewidth=0.8)
    if len(deriv_peaks) > 0:
        ax2.plot(i_data[deriv_peaks], dv[deriv_peaks] * R_PRE, 'ro', markersize=3)
    ax2.set_ylabel('$dV/dI$ [$\\Omega$]')
    ax2.set_xlabel('Bias [Reference V]')
    ax2.grid(True, ls='--', alpha=0.3)

    ax3.fill_between(v_grid * 1e6, density, alpha=0.3, color='green')
    ax3.plot(v_grid * 1e6, density, 'g-', linewidth=1.2, label='KDE density')
    if len(kde_peaks) > 0:
        ax3.plot(v_grid[kde_peaks] * 1e6, density[kde_peaks], 'mo',
                 markersize=6, label=f'Plateaus ({len(kde_peaks)})')
    ax3.set_xlabel('$V_{\\mathrm{SQUID}}$ [$\\mu$V]')
    ax3.set_ylabel('Density')
    info = f'$\\Delta V_{{\\mathrm{{KDE}}}}$ = {step_kde*1e6:.1f} $\\mu$V'
    if step_deriv > 0:
        info += f'\n$\\Delta V_{{\\mathrm{{deriv}}}}$ = {step_deriv*1e6:.1f} $\\mu$V'
    ax3.text(0.02, 0.95, info, transform=ax3.transAxes, fontsize=9,
             verticalalignment='top',
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))
    ax3.legend(loc='upper right', fontsize=8, frameon=False)
    ax3.grid(True, ls='--', alpha=0.3)

    plt.tight_layout()

    if plot_dir is None:
        base, _ = os.path.splitext(filepath)
        plot_path = f"{base}_kde_verification.png"
    else:
        basename = os.path.splitext(os.path.basename(filepath))[0]
        plot_path = os.path.join(plot_dir, f"{basename}_kde_verification.png")

    plt.savefig(plot_path, dpi=150, bbox_inches='tight')
    plt.close()
    return plot_path


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python shapiro_kde.py <data_file.txt> [--plot]")
    else:
        do_plot = '--plot' in sys.argv
        filepath = sys.argv[1]
        step_kde, step_deriv, n_kde, n_deriv = extract_shapiro_step_kde(
            filepath, save_plot=do_plot)
        print(f"KDE step: {step_kde*1e6:.2f} uV ({n_kde} peaks)")
        print(f"Derivative step: {step_deriv*1e6:.2f} uV ({n_deriv} transitions)")
