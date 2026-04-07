import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.signal import find_peaks, savgol_filter
from pathlib import Path

def analyze_zero_field():
    # Setup paths
    root = Path(__file__).resolve().parent
    data_path = root / "code/time-resolved-odmr/results/CW_SweepREDO.csv"
    output_dir = root / "code/time-resolved-odmr/results/analysis/plots"
    output_dir.mkdir(parents=True, exist_ok=True)

    if not data_path.exists():
        print(f"Error: Could not find {data_path}")
        return

    # Load data
    df = pd.read_csv(data_path)
    x = df["freq_GHz"].to_numpy()
    y = df["R_V"].to_numpy()

    # Smoothing for peak detection
    y_smooth = savgol_filter(y, window_length=15, polyorder=2)
    
    # Peak detection - being more sensitive to find the two strained resonances
    # Adjusting prominence to find precisely two peaks
    prominence = (np.max(y_smooth) - np.min(y_smooth)) * 0.15
    peaks, _ = find_peaks(y_smooth, prominence=prominence, distance=5)
    
    print(f"Detected {len(peaks)} peaks in zero-field sweep.")
    
    if len(peaks) >= 2:
        # Sort by frequency to identify f1 and f2
        peak_freqs = sorted(x[peaks[:2]])
        f1, f2 = peak_freqs[0], peak_freqs[1]
        D_val = (f1 + f2) / 2
        E_val = (f2 - f1) / 2
        print(f"Extracted Parameters:\nD = {D_val:.4f} GHz\nE = {E_val*1e3:.2f} MHz")
    else:
        print("Warning: Could not find two distinct peaks. Using default benchmarks.")
        D_val, E_val = 2.8708, 0.00275

    # Plotting
    fig, ax = plt.subplots(figsize=(10, 5), dpi=120)
    
    # Raw data as a clean line
    ax.plot(x, y * 1e3, "-", lw=2, color="#457B9D", label="Measured Signal")
    
    # Benchmarks
    ax.axvline(D_val - E_val, color="red", ls="--", alpha=0.7, label=f"f1 = {D_val-E_val:.4f} GHz")
    ax.axvline(D_val + E_val, color="green", ls="--", alpha=0.7, label=f"f2 = {D_val+E_val:.4f} GHz")
    
    # Labels
    param_text = f"$D$ = {D_val:.4f} GHz\n$E$ = {E_val*1e3:.2f} MHz"
    ax.text(0.02, 0.45, param_text, transform=ax.transAxes, 
            bbox=dict(facecolor='white', alpha=0.9, edgecolor='gray'), 
            fontsize=12, fontweight='bold')
    
    ax.set_title("CW Frequency Sweep (Zero Magnetic Field)", fontweight="bold", fontsize=14)
    ax.set_xlabel("Microwave Frequency (GHz)", fontweight="bold")
    ax.set_ylabel("Signal Amplitude (mV)", fontweight="bold")
    ax.grid(True, which="both", ls=":", alpha=0.5)
    ax.legend(loc="upper right", frameon=True)
    
    fig.tight_layout()
    plot_path = output_dir / "CW_SweepREDO_analysis.pdf"
    plt.savefig(plot_path)
    print(f"\nPlot saved to: {plot_path}")

if __name__ == "__main__":
    analyze_zero_field()
