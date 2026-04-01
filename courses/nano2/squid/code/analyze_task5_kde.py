"""
Task 5: Frequency dependence of Shapiro steps using KDE extraction.
Replaces analyze_task5.py with robust KDE method.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from shapiro_kde import extract_shapiro_step_kde

# Frequencies and corresponding file naming
freqs_ghz = [8, 9, 9.5, 10, 11, 11.5, 12]
freq_strs = ["8ghz", "9ghz", "9.5ghz", "10ghz", "11ghz", "11-5ghz", "12ghz"]

voltages_kde = []
voltages_deriv = []
n_peaks_kde = []
valid_freqs = []

print("=" * 60)
print("Task 5: KDE-based Frequency Dependence Analysis")
print("=" * 60)

for f_ghz, f_str in zip(freqs_ghz, freq_strs):
    filepath = f"task5/task4_shapiro_{f_str}_restored.txt"
    print(f"\n--- {f_ghz} GHz ---")
    try:
        s_kde, s_deriv, n_kde, n_d = extract_shapiro_step_kde(
            filepath, sigma=5, save_plot=True)
        print(f"  KDE:   {s_kde*1e6:.2f} uV ({n_kde} peaks)")
        print(f"  Deriv: {s_deriv*1e6:.2f} uV ({n_d} transitions)")

        if s_kde > 0:
            voltages_kde.append(s_kde)
            valid_freqs.append(f_ghz)
            voltages_deriv.append(s_deriv)
            n_peaks_kde.append(n_kde)
        elif s_deriv > 0:
            voltages_kde.append(s_deriv)
            valid_freqs.append(f_ghz)
            voltages_deriv.append(s_deriv)
            n_peaks_kde.append(n_d)
        else:
            print(f"  WARNING: No valid step extracted at {f_ghz} GHz")
    except Exception as e:
        print(f"  FAILED: {e}")

valid_freqs = np.array(valid_freqs) * 1e9  # Hz
voltages = np.array(voltages_kde)

# Linear fit through origin: V = Phi_0 * f => Phi_0 = sum(f*V)/sum(f^2)
phi0_measured = np.sum(valid_freqs * voltages) / np.sum(valid_freqs**2)
phi0_theory = 2.067833848e-15  # Wb

# Weighted fit (weight by number of KDE peaks = proxy for data quality)
weights = np.array(n_peaks_kde, dtype=float)
weights = np.maximum(weights, 1)  # avoid zero weights
phi0_weighted = np.sum(weights * valid_freqs * voltages) / np.sum(weights * valid_freqs**2)

# Error statistics
residuals = voltages - phi0_measured * valid_freqs
rss = np.sum(residuals**2)
rmse = np.sqrt(np.mean(residuals**2))

print(f"\n{'=' * 60}")
print(f"RESULTS")
print(f"{'=' * 60}")
print(f"Frequencies used: {len(valid_freqs)}/{len(freqs_ghz)}")
print(f"Unweighted Phi_0: {phi0_measured:.4e} Wb")
print(f"Weighted Phi_0:   {phi0_weighted:.4e} Wb")
print(f"Theoretical:      {phi0_theory:.4e} Wb")
print(f"Unweighted error: {abs(phi0_measured - phi0_theory)/phi0_theory*100:.2f}%")
print(f"Weighted error:   {abs(phi0_weighted - phi0_theory)/phi0_theory*100:.2f}%")
print(f"RSS:  {rss:.4e}")
print(f"RMSE: {rmse*1e6:.2f} uV")

# Plot
fig, ax = plt.subplots(figsize=(7, 5))
ax.errorbar(valid_freqs / 1e9, voltages * 1e6, fmt='ko', markersize=7,
            capsize=3, label='KDE extraction')

fit_x = np.linspace(0, 13, 100)
ax.plot(fit_x, phi0_measured * fit_x * 1e9 * 1e6, 'r--', linewidth=1.5,
        label='Linear fit (through origin)')
ax.plot(fit_x, phi0_theory * fit_x * 1e9 * 1e6, 'b:', linewidth=1.0, alpha=0.6,
        label=f'Theory ($\\Phi_0 = {phi0_theory:.3e}$ Wb)')

ax.set_xlabel('Microwave Frequency $\\nu$ [GHz]')
ax.set_ylabel('Voltage Step $\\Delta V$ [$\\mu$V]')
ax.set_title('Frequency Dependence of Shapiro Step Voltage')
ax.set_xlim(0, 13)
ax.set_ylim(0, max(voltages * 1e6) * 1.3)
ax.grid(True, ls='--', alpha=0.3)

textstr = '\n'.join([
    f'$\\Phi_0^{{\\mathrm{{meas}}}} = {phi0_measured:.3e}$ Wb',
    f'$\\Phi_0^{{\\mathrm{{theo}}}} = {phi0_theory:.3e}$ Wb',
    f'Error: {abs(phi0_measured - phi0_theory)/phi0_theory*100:.1f}%',
    f'RMSE: {rmse*1e6:.1f} $\\mu$V'
])
props = dict(boxstyle='round', facecolor='white', alpha=0.9, edgecolor='gray')
ax.text(0.05, 0.95, textstr, transform=ax.transAxes, fontsize=9,
        verticalalignment='top', bbox=props)
ax.legend(loc='lower right', fontsize=9)
plt.tight_layout()

save_path = "task5/task5_frequency_dependence_kde.png"
plt.savefig(save_path, dpi=200)
plt.close()
print(f"\nPlot saved: {save_path}")
