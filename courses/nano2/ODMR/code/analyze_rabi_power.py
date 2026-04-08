import matplotlib
matplotlib.use('Agg')
import numpy as np

import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Data provided by user
# Attenuation corresponds to: 0 dB (no atten), 6 dB, 10 dB.
# Rabi frequency values (likely MHz)
attenuation_db = np.array([0, 6, 10])
f_rabi = np.array([2.48, 2.17, 1.46])

# Conversion to relative amplitude (voltage ratio)
# P_rel = 10^(-A/10)  => sqrt(P_rel) = 10^(-A/20)
# Since f_Rabi is proportional to sqrt(P), we plot against sqrt(P_rel)
relative_amplitude = 10**(-attenuation_db / 20.0)

# Theoretical model: f_Rabi = k * sqrt(P)
def linear_model(x, k):
    return k * x

# Perform the fit
popt, pcov = curve_fit(linear_model, relative_amplitude, f_rabi)
k_fit = popt[0]
k_err = np.sqrt(pcov[0,0])

# Generate smooth curve for plotting the fit
x_fit = np.linspace(0, 1.1 * np.max(relative_amplitude), 100)
y_fit = linear_model(x_fit, k_fit)

# Output results
print(f"Results of the Power Dependence Fit (f_Rabi vs. sqrt(P_rel)):")
print(f"----------------------------------------------------------")
print(f"Attenuation (dB): {attenuation_db}")
print(f"Relative Amplitude (sqrt(P)): {np.array2string(relative_amplitude, precision=4, separator=', ')}")
print(f"Rabi Frequencies (f_Rabi): {f_rabi}")
print(f"Fit coefficient (k): {k_fit:.4f} +/- {k_err:.4f}")
print(f"----------------------------------------------------------")

# Plotting with Premium Aesthetics
plt.style.use('default') 
fig, ax = plt.subplots(figsize=(8, 6), dpi=300)

# Custom color palette (sleek dark mode / high contrast colors)
point_color = '#E63946' # Red-ish
line_color = '#1D3557'  # Dark Blue

# Plot points and fit line
ax.scatter(relative_amplitude, f_rabi, color=point_color, s=100, label='Experiment Data', zorder=5, edgecolor='black', alpha=0.9)
ax.plot(x_fit, y_fit, color=line_color, linewidth=2.5, linestyle='--', label=f'Linear Fit (k={k_fit:.2f})', zorder=4)

# Labels and Titles
ax.set_title("Rabi Frequency Power Dependence", fontsize=16, fontweight='bold', pad=15)
ax.set_xlabel(r"Relative Microwave Amplitude ($V_{\text{MW}} \propto \sqrt{P_{\text{MW}}} = 10^{-A_{\text{dB}}/20}$)", fontsize=12)
ax.set_ylabel(r"Rabi Frequency $f_{\text{Rabi}}$ [MHz]", fontsize=12)

# Grid and Styling
ax.grid(True, linestyle=':', alpha=0.6)
ax.legend(frameon=True, fontsize=10, loc='lower right')

# Set aesthetic limits
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 1.2 * np.max(f_rabi))

# Tight layout and save as HD PDF
plt.tight_layout()
output_filename = "figures/rabi_power_dependence.pdf"
plt.savefig(output_filename, format='pdf', bbox_inches='tight')
plt.show()

print(f"Successfully saved plot to {output_filename}")
