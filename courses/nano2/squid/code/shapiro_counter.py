import sys
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from scipy.signal import find_peaks

def count_shapiro_steps(filepath, sigma=5, height_threshold=None, save_files=True):
    # Minimalist data load (time, V_squid, V_ref)
    try:
        data = np.loadtxt(filepath, skiprows=1)
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # V_ref is proportional to current, V_squid is the signal

    length = len(data)

    # inner 80% of data
    start = 0.1
    end = 1 - start

    v_sq = data[int(length*start):int(length*end), 1] / 1e3 # Account for amplifier gain of 1000
    v_ref = data[int(length*start):int(length*end), 2]

    # Evaluate data directly in time to retain temporal sweep structure
    # and avoid "interleaving" noise from sorting discrete noisy data
    i_sweep = v_ref
    v_sweep = v_sq

    # 1. Smooth the data directly in the time domain
    v_smooth = gaussian_filter(v_sweep, sigma=sigma)
    i_smooth = gaussian_filter(i_sweep, sigma=sigma)  # Smooth out current noise

    # 2. Numerical derivative (dV/dI) calculated parametrically (dV/dt) / (dI/dt)
    di = np.gradient(i_smooth)
    dv = np.gradient(v_smooth) / np.where(di == 0, 1e-12, di)
    
    # Extra slight smoothing to the derivative to suppress measurement spikes
    dv = gaussian_filter(dv, sigma=3)

    # 3. Method A: Edge detection using Prominence in the Derivative
    # Using 'prominence' is much more scientifically robust than an arbitrary 'height' 
    # as it looks for peaks that stand out from the local baseline noise.
    prominence_threshold = np.std(dv) * 0.5
    peaks, _ = find_peaks(dv, prominence=prominence_threshold, distance=10)
    
    num_steps = len(peaks)
    
    # 4. Method B: Voltage Histogram Analysis (Density of States)
    # The voltage dwells on the Shapiro step plateaus, creating density peaks.
    # The distance between these peaks is exactly the voltage step. This avoids
    # taking derivatives of heavily noisy experimental data entirely!
    hist, bin_edges = np.histogram(v_sweep, bins=300)
    bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
    # Smooth the histogram to easily locate the centers of the populations
    hist_smooth = gaussian_filter(hist, sigma=2)
    # Find peaks in the histogram (the voltage plateaus)
    hist_peaks, _ = find_peaks(hist_smooth, prominence=np.max(hist_smooth)*0.08)
    
    if save_files:
        print(f"\n--- Scientific Shapiro Analysis: {filepath} ---")
    
    avg_step_dv = 0
    if num_steps > 1:
        v_at_edges = v_sweep[peaks]
        # Edges denote the boundaries; distance between edges is the plateau step
        # Using median of absolute difference to be physically robust against noise/turnarounds
        avg_step_dv = np.median(np.abs(np.diff(v_at_edges)))
        if save_files:
            print(f"Method A (Derivative Peaks): {num_steps} transitions identified.")
            print(f" -> Average Voltage Step: {avg_step_dv*1e6:.2f} uV")

    avg_step_hist = 0
    if len(hist_peaks) > 1:
        plateau_voltages = bin_centers[hist_peaks]
        # Robust median absolute extraction
        avg_step_hist = np.median(np.abs(np.diff(plateau_voltages)))
        if save_files:
            print(f"Method B (Voltage Histogram): {len(hist_peaks)} plateaus identified.")
            print(f" -> Average Voltage Step: {avg_step_hist*1e6:.2f} uV")

    if save_files:
        # Save the analysis summary to a text file in the same directory
        base, _ = os.path.splitext(filepath)
        report_name = f"{base}_analysis.txt"
        with open(report_name, "w") as f:
            f.write(f"--- Scientific Shapiro Analysis: {filepath} ---\n")
            f.write(f"Method A (Derivative Peaks): {num_steps} transitions identified.\n")
            if num_steps > 1:
                f.write(f" -> Average Voltage Step: {avg_step_dv*1e6:.2f} uV\n")
            f.write(f"Method B (Voltage Histogram): {len(hist_peaks)} plateaus identified.\n")
            if len(hist_peaks) > 1:
                f.write(f" -> Average Voltage Step: {avg_step_hist*1e6:.2f} uV\n")

        print(f"\nAnalysis report saved to: {report_name}")

        # Clean viz check
        plot_shapiro(i_smooth, v_sweep, dv, peaks, hist_smooth, bin_centers, hist_peaks, filepath)
    
    return avg_step_dv, avg_step_hist

def plot_shapiro(i, v, dv, peaks, hist_smooth, bin_centers, hist_peaks, title):
    """Robust scientific plotter for Shapiro verification."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 9), gridspec_kw={'height_ratios': [2, 1, 1]})
    
    # Raw V-I Curve
    ax1.plot(i, v, 'k-', alpha=0.8, label="V(I) data")
    ax1.plot(i[peaks], v[peaks], 'rx', markersize=6, label="Derivative Transitions (Method A)")
    ax1.set_ylabel("SQUID Voltage [V]", fontweight='bold')
    ax1.set_title(f"Shapiro Verification: {title}", pad=15)
    ax1.legend(loc='lower right', frameon=False, fontsize='small')
    ax1.grid(True, linestyle='--', alpha=0.5)

    # Differential Resistance dV/dI
    ax2.plot(i, dv, 'b-', alpha=0.6, label="dV/dI (smoothed)")
    ax2.plot(i[peaks], dv[peaks], 'ro', markersize=4, label="Transitions")
    ax2.set_xlabel("Bias [Reference V]", fontweight='bold')
    ax2.set_ylabel("dV/dI [a.u.]", fontweight='bold')
    ax2.legend(loc='upper right', frameon=False, fontsize='small')
    ax2.grid(True, linestyle='--', alpha=0.5)

    # Voltage Histogram (Density of States)
    ax3.plot(bin_centers, hist_smooth, 'g-', alpha=0.8, label="Voltage Histogram")
    ax3.plot(bin_centers[hist_peaks], hist_smooth[hist_peaks], 'mo', markersize=5, label="Identified Plateaus (Method B)")
    ax3.set_xlabel("SQUID Voltage [V]", fontweight='bold')
    ax3.set_ylabel("Density / Count", fontweight='bold')
    ax3.legend(loc='upper right', frameon=False, fontsize='small')
    ax3.grid(True, linestyle='--', alpha=0.5)
    
    plt.tight_layout()
    
    plt.tight_layout()
    
    # Save plot to file in the same directory
    base, _ = os.path.splitext(title)
    plot_name = f"{base}_verification.png"
    plt.savefig(plot_name, dpi=150)
    print(f"Verification plot saved to: {plot_name}")
    
    # Attempt show, but don't fail if non-interactive
    try:
        plt.show()
    except Exception:
        pass

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python shapiro_counter.py <data_file.txt>")
    else:
        count_shapiro_steps(sys.argv[1])
