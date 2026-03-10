import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from shapiro_counter import count_shapiro_steps

# Given frequencies in GHz
freqs_ghz = [8, 9, 9.5, 10, 11, 11.5, 12]
freq_strs = ["8ghz", "9ghz", "9.5ghz", "10ghz", "11ghz", "11-5ghz", "12ghz"]

voltages_a = []
voltages_b = []
valid_freqs = []

for f_ghz, f_str in zip(freqs_ghz, freq_strs):
    filepath = f"task5/task4_shapiro_{f_str}_restored.txt" # Intentionally addressing the naming anomaly
    print(f"\nProcessing {f_ghz} GHz...")
    try:
        avg_dv, avg_hist = count_shapiro_steps(filepath, sigma=5)
        if avg_dv > 0:
            voltages_a.append(avg_dv)
            voltages_b.append(avg_hist)
            valid_freqs.append(f_ghz)
    except Exception as e:
        print(f"Failed to process {filepath}: {e}")

# Convert lists to arrays
valid_freqs = np.array(valid_freqs) * 1e9  # Convert GHz to Hz
voltages = np.array(voltages_a)            # Measured voltage steps (Using Method A)

# Linear Fit through ORIGIN: V = Phi_0 * f
# Phi_0 = sum(f*V) / sum(f^2)
slope = np.sum(valid_freqs * voltages) / np.sum(valid_freqs**2)

theoretical_phi0 = 2.067833848e-15 # Wb

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(valid_freqs / 1e9, voltages * 1e6, 'bo', label="Measured Values (Method A)", markersize=8)

# Fit line
fit_x = np.linspace(0, max(valid_freqs), 100)
fit_y = slope * fit_x
ax.plot(fit_x / 1e9, fit_y * 1e6, 'r--', label=f"Linear Fit (Through Origin)")

ax.set_title("Frequency Dependence of Shapiro Step Voltage", fontweight='bold', pad=15)
ax.set_xlabel("Microwave Frequency [GHz]", fontweight='bold')
ax.set_ylabel(r"Voltage Step Size $\Delta V$ [$\mu$V]", fontweight='bold')
ax.set_xlim(0, max(valid_freqs / 1e9) + 1)
ax.set_ylim(0, max(voltages * 1e6) + 5)
ax.grid(True, linestyle='--', alpha=0.5)

# Text box with physics constants
textstr = '\n'.join((
    r'Fit Model: $\Delta V = \Phi_0 \cdot \nu$',
    f'Measured $\\Phi_0 = {slope:.4e}$ Wb',
    f'Theoretical $\\Phi_0 = {theoretical_phi0:.4e}$ Wb',
    f'Error margin = {abs(slope - theoretical_phi0)/theoretical_phi0*100:.2f}%'
))
props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray')
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props)

ax.legend(loc='lower right')
plt.tight_layout()

save_path = "task5/task5_frequency_dependence.png"
plt.savefig(save_path, dpi=200)
print(f"\n====================================")
print(f"Task 5 Analysis Complete!")
print(f"Measured Phi_0: {slope:.4e} Wb")
print(f"Theoretical:    {theoretical_phi0:.4e} Wb")
print(f"Error:          {abs(slope - theoretical_phi0)/theoretical_phi0*100:.2f}%")
print(f"Plot saved to:  {save_path}")
print(f"====================================")
