"""
Task 6: Power dependence analysis using KDE extraction.
28 measurements at 10 GHz at increasing microwave power.
"""
import os
import sys
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shapiro_kde import extract_shapiro_step_kde

# Reference power anchor points
N_ref = np.array([0, 4, 8, 12, 16, 20, 24, 28])
P_ref = np.array([-26.1, -10.4, -5.5, -1.1, 1.8, 4.6, 7.5, 11.7])

# 3rd order polynomial fit for power mapping
coeffs = np.polyfit(N_ref, P_ref, 3)
poly = np.poly1d(coeffs)
rss_poly = np.sum((P_ref - poly(N_ref))**2)

print(f"Polynomial coefficients: a3={coeffs[0]:.4e}, a2={coeffs[1]:.4e}, "
      f"a1={coeffs[2]:.4e}, a0={coeffs[3]:.4e}")
print(f"RSS = {rss_poly:.3f}")

# Process temp_cyc files
task6_dir = "task6"
N_meas = []
P_meas = []
DV_meas = []
n_peaks_all = []

print(f"\n{'='*60}")
print(f"Task 6: KDE-based Power Dependence (10 GHz)")
print(f"{'='*60}")

for idx in range(28):
    filepath = os.path.join(task6_dir, f"temp_cyc_{idx}.txt")
    if not os.path.exists(filepath):
        print(f"  [{idx:2d}] File missing")
        continue
    try:
        s_kde, s_deriv, n_kde, n_d = extract_shapiro_step_kde(filepath, sigma=5)
        p_dbm = poly(idx)
        if s_kde > 0:
            N_meas.append(idx)
            P_meas.append(p_dbm)
            DV_meas.append(s_kde * 1e6)
            n_peaks_all.append(n_kde)
            print(f"  [{idx:2d}] P={p_dbm:6.1f} dBm  ΔV={s_kde*1e6:7.1f} µV  ({n_kde} peaks)")
        else:
            print(f"  [{idx:2d}] P={p_dbm:6.1f} dBm  No valid step")
    except Exception as e:
        print(f"  [{idx:2d}] FAILED: {e}")

N_meas = np.array(N_meas)
P_meas = np.array(P_meas)
DV_meas = np.array(DV_meas)
n_peaks_all = np.array(n_peaks_all)

print(f"\nValid: {len(N_meas)}/28")
print(f"ΔV range: {np.min(DV_meas):.1f} – {np.max(DV_meas):.1f} µV")
print(f"ΔV mean ± std: {np.mean(DV_meas):.1f} ± {np.std(DV_meas):.1f} µV")

# Plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 7), gridspec_kw={'height_ratios': [1, 1.2]})

# Panel 1: Power mapping
N_fine = np.linspace(0, 28, 200)
ax1.plot(N_fine, poly(N_fine), 'r--', linewidth=1.5, label=f'Cubic $P(N)$, RSS={rss_poly:.1f}')
ax1.plot(N_ref, P_ref, 'ro', markersize=8, zorder=5, label='Anchor points')
ax1.set_xlabel('Measurement Index $N$')
ax1.set_ylabel('Power $P$ [dBm]')
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, ls='--', alpha=0.3)
ax1.set_title('Task 6: Power Dependence at 10 GHz')

# Panel 2: ΔV vs P(N)
scatter = ax2.scatter(P_meas, DV_meas, c=n_peaks_all, cmap='viridis',
                       s=50, edgecolors='k', linewidths=0.5, zorder=5)
cbar = plt.colorbar(scatter, ax=ax2, label='# KDE peaks')
ax2.axhline(y=20.7, color='r', linestyle=':', alpha=0.5,
            label='$\\Phi_0 \\cdot 10$ GHz = 20.7 µV')
ax2.set_xlabel('Microwave Power $P$ [dBm]')
ax2.set_ylabel('Voltage Step $\\Delta V$ [µV]')
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, ls='--', alpha=0.3)

# Annotate statistics
stats = (f'Valid: {len(N_meas)}/28\n'
         f'$\\Delta V$ = {np.mean(DV_meas):.1f} ± {np.std(DV_meas):.1f} µV')
ax2.text(0.97, 0.05, stats, transform=ax2.transAxes, fontsize=9,
         ha='right', va='bottom',
         bbox=dict(boxstyle='round', fc='white', alpha=0.9, ec='gray'))

plt.tight_layout()
save_path = os.path.join(task6_dir, "task6_power_kde.png")
plt.savefig(save_path, dpi=200, bbox_inches='tight')
plt.close()
print(f"\nPlot saved: {save_path}")
