import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.interpolate import griddata

# Set up matplotlib style to mimic the SQUID report
plt.rcParams.update({
    "text.usetex": False,
    "font.family": "serif",
    "font.serif": ["Computer Modern Roman", "Times New Roman", "serif"],
    "font.size": 12,
    "axes.labelsize": 14,
    "axes.titlesize": 14,
    "legend.fontsize": 12,
    "xtick.labelsize": 12,
    "ytick.labelsize": 12,
})

# Task 3 Marginals
angles_marg = np.array([4, 4.9, 5.5, 6, 6.5, 6.8, 7.2, 7.5, 7.9, 8.3, 9])
counts_marg = np.array([26500, 27000, 30500, 36000, 80050, 156000, 256000, 230000, 178000, 160000, 130000])

# Sort
sort_idx = np.argsort(angles_marg)
angles_marg = angles_marg[sort_idx]
counts_marg = counts_marg[sort_idx]

# 2D Sweep Data (furthest, closest, mean_coincidence)
# Parsed directly from lab_notes.md
data_2d = [
    # furthest 6.7
    (6.7, 6, np.mean([1,2,1])), (6.7, 6.3, np.mean([1,1,2])), (6.7, 6.5, np.mean([2,3,2])), (6.7, 6.75, np.mean([6,1,6])),
    (6.7, 7.0, np.mean([5,4,5])), (6.7, 7.2, np.mean([1,7,1])), (6.7, 7.4, np.mean([5,4,6])), (6.7, 7.8, np.mean([3,5,0])),
    (6.7, 8.2, np.mean([2,2,1])), (6.7, 8.6, np.mean([0,1,0])), (6.7, 9.1, np.mean([0,1,0])),
    # furthest 6.85
    (6.85, 9.25, np.mean([2,1,1])), (6.85, 8.7, np.mean([1,3,6])), (6.85, 8.4, np.mean([5,7,7])), (6.85, 8.1, np.mean([11,8,8])),
    (6.85, 7.8, np.mean([4,3,6])), (6.85, 7.6, np.mean([3,5,6])), (6.85, 7.4, np.mean([14,6,7])), (6.85, 7.2, np.mean([3,5,8])),
    (6.85, 6.9, np.mean([6,4,2])), (6.85, 6.6, np.mean([9,4,6])), (6.85, 6.3, np.mean([1,3,2])), (6.85, 6, np.mean([2,0,1])),
    # furthest 7.0
    (7.0, 10, np.mean([0,1,1])), (7.0, 9.7, np.mean([1,2,1])), (7.0, 9.4, np.mean([1,0,0])), (7.0, 9.1, np.mean([1,2,3])),
    (7.0, 8.8, np.mean([5,3,4])), (7.0, 8.5, np.mean([9,7,13])), (7.0, 8.2, np.mean([17,18,22])), (7.0, 7.9, np.mean([23,25,22])),
    (7.0, 7.7, np.mean([24,22,23])), (7.0, 7.4, np.mean([27,19,21])), (7.0, 7.1, np.mean([22,38,16])), (7.0, 6.8, np.mean([32,34,26])),
    (7.0, 6.5, np.mean([20,23,20])), (7.0, 6.2, np.mean([11,15,8])), (7.0, 6, np.mean([6,1,2])),
    # furthest 7.15
    (7.15, 5.2, np.mean([6,11,5])), (7.15, 5.7, np.mean([21,7,12])), (7.15, 5.9, np.mean([13,6,12])), (7.15, 6.1, np.mean([46,32,41])),
    (7.15, 6.2, np.mean([40,42,35])), (7.15, 6.35, np.mean([102,80,72])), (7.15, 6.5, np.mean([198,218,223])), (7.15, 6.6, np.mean([240,252,248])),
    (7.15, 6.8, np.mean([239,228,258])), (7.15, 7, np.mean([246,243,245])), (7.15, 7.3, np.mean([219,196,205])), (7.15, 7.5, np.mean([162,182,160])),
    (7.15, 7.6, np.mean([149,187,152])), (7.15, 7.8, np.mean([139,147,155])), (7.15, 8, np.mean([110,106,137])), (7.15, 8.1, np.mean([126,114,121])),
    (7.15, 8.3, np.mean([117,101,124])), (7.15, 8.4, np.mean([105,106,89])), (7.15, 8.5, np.mean([90,87,88])), (7.15, 8.8, np.mean([64,63,84])),
    (7.15, 9, np.mean([57,41,35])), (7.15, 9.2, np.mean([23,24,21])), (7.15, 9.5, np.mean([10,10,12])), (7.15, 9.75, np.mean([10,8,6])),
    (7.15, 10, np.mean([5,8,5])), (7.15, 10.2, np.mean([4,5,9])), (7.15, 10.5, np.mean([6,5,7])), (7.15, 11, np.mean([1,7,6])),
    (7.15, 7.1, np.mean([199, 212, 211])), (7.15, 7.7, np.mean([144, 151, 160])), (7.15, 7.9, np.mean([151, 130, 147])),
    (7.15, 8.2, np.mean([125, 104, 118])), (7.15, 8.7, np.mean([93, 82, 83])), (7.15, 8.9, np.mean([56, 72, 75])),
    (7.15, 9.1, np.mean([38, 32, 30])), (7.15, 9.3, np.mean([10, 6, 5])), (7.15, 9.4, np.mean([4, 3, 6])), (7.15, 9.6, np.mean([0, 0, 0])),
    # furthest 7.3
    (7.3, 5.2, np.mean([2,1,1])), (7.3, 5.4, np.mean([1,2,1])), (7.3, 5.6, np.mean([1,0,1])), (7.3, 6.0, np.mean([2,0,3])),
    (7.3, 6.5, np.mean([12,17,9])), (7.3, 6.8, np.mean([10,11,6])), (7.3, 7, np.mean([11,12,4])), (7.3, 7.2, np.mean([12,6,14])),
    (7.3, 7.4, np.mean([6,7,13])), (7.3, 7.6, np.mean([4,6,8])), (7.3, 7.8, np.mean([9,12,14])), (7.3, 8, np.mean([13,12,13])),
    (7.3, 8.2, np.mean([13,17,7])), (7.3, 8.6, np.mean([18,17,21])), (7.3, 9, np.mean([11,22,17])), (7.3, 9.2, np.mean([14,8,5])),
    (7.3, 9.4, np.mean([3,7,4])), (7.3, 9.7, np.mean([1,2,1])),
    # furthest 7.4
    (7.4, 9.4, np.mean([8,3,5])), (7.4, 9.6, np.mean([4,5,5])), (7.4, 9.9, np.mean([3,2,3])), (7.4, 9.2, np.mean([12,13,9])),
    (7.4, 8.9, np.mean([15,11,19])), (7.4, 8.7, np.mean([20,17,18])), (7.4, 8.5, np.mean([24,18,20])), (7.4, 8.2, np.mean([19,16,8])),
    (7.4, 8, np.mean([16,21,13])), (7.4, 7.8, np.mean([8,9,13])), (7.4, 7.5, np.mean([9,10,7])), (7.4, 7.2, np.mean([14,12,18])),
    (7.4, 6.8, np.mean([13,17,19])),
    # furthest 7.6
    (7.6, 10, np.mean([6,7,7])), (7.6, 10.3, np.mean([5,3,4])), (7.6, 9.8, np.mean([5,8,10])), (7.6, 9.6, np.mean([11,17,11])),
    (7.6, 9.4, np.mean([16,11,12])), (7.6, 9.2, np.mean([7,13,12])), (7.6, 9, np.mean([18,14,12])), (7.6, 8.8, np.mean([11,13,8])),
    (7.6, 8.6, np.mean([13,6,11])), (7.6, 8.3, np.mean([10,6,8])), (7.6, 8, np.mean([4,5,2])), (7.6, 7.7, np.mean([2,1,7])),
    (7.6, 7.4, np.mean([8,2,4])),
    # furthest 7.7
    (7.7, 7.4, np.mean([3,1,2])), (7.7, 7.65, np.mean([1,0,4])), (7.7, 7.9, np.mean([3,1,3])), (7.7, 8.2, np.mean([3,1,3])),
    (7.7, 8.75, np.mean([3,10,8])), (7.7, 10.5, np.mean([4,4,3])), (7.7, 10.2, np.mean([5,2,7])), (7.7, 10, np.mean([10,7,5])),
    (7.7, 9.8, np.mean([6,9,8])), (7.7, 9.5, np.mean([8,10,15])), (7.7, 9.2, np.mean([11,16,8])), (7.7, 9, np.mean([7,10,11]))
]

x = np.array([d[0] for d in data_2d])
y = np.array([d[1] for d in data_2d])
z = np.array([d[2] for d in data_2d])

# Create a grid
xi = np.linspace(6.5, 7.9, 100)
yi = np.linspace(5.0, 11.2, 100)
xi, yi = np.meshgrid(xi, yi)
zi = griddata((x, y), z, (xi, yi), method='linear')

os.makedirs('figures', exist_ok=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot 1: Marginals
ax1.plot(angles_marg, counts_marg, 'ko-', markersize=4, linewidth=1.5)
ax1.set_xlabel(r'Angular Position $\theta$ ($^\circ$)')
ax1.set_ylabel(r'Marginal Count Rate (cps)')
ax1.set_title(r'Single-Photon Intensity Distribution')
ax1.grid(True, linestyle='--', alpha=0.6)

# Find half opening angle (approx peak)
peak_idx = np.argmax(counts_marg)
phi_0 = angles_marg[peak_idx]
ax1.axvline(phi_0, color='r', linestyle='--', label=rf'Peak $\approx {phi_0}^\circ$')
ax1.legend()

# Plot 2: 2D Heatmap
im = ax2.pcolormesh(xi, yi, zi, shading='auto', cmap='viridis')
ax2.scatter(x, y, c='k', s=2, alpha=0.3, label='Data points') # show where data actually is
ax2.set_xlabel(r'Fixed Detector Angle ($^\circ$)')
ax2.set_ylabel(r'Scanning Detector Angle ($^\circ$)')
ax2.set_title(r'Correlated Coincidence Distribution')
fig.colorbar(im, ax=ax2, label='Coincidence Rate (cps)')
ax2.legend()

plt.tight_layout()
plt.savefig('figures/task3_geometry.pdf', bbox_inches='tight')
print("Task 3 figures saved to figures/task3_geometry.pdf")
