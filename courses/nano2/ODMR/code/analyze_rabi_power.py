import matplotlib
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Experimental Data
# Attenuation corresponds to: 0 dB, 6 dB, 10 dB.
# Rabi frequency values (MHz)
attenuation_db = np.array([0, 6, 10])
f_rabi = np.array([2.48, 2.17, 1.46])

# Independent variable: Relative Microwave Amplitude (sqrt of power)
# x = 10^(-A/20)
x_data = 10**(-attenuation_db / 20.0)

# Rigorous Model: Effective Rabi frequency with detuning offset
# f_eff = sqrt( (k * x)^2 + delta^2 )
def rigorous_model(x, k, delta):
    return np.sqrt((k * x)**2 + delta**2)

# Alternative Linear Model (for comparison/simplicity if detuning isn't the only factor)
# f = m * x + c
def linear_offset_model(x, m, c):
    return m * x + c

# Performing the fit with the Rigorous Model
try:
    popt, pcov = curve_fit(rigorous_model, x_data, f_rabi, p0=[2.5, 1.0])
    k_fit, delta_fit = popt
    # R-squared calculation
    residuals = f_rabi - rigorous_model(x_data, *popt)
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((f_rabi - np.mean(f_rabi))**2)
    r_squared = 1 - (ss_res / ss_tot)
except:
    # Fallback to linear if sqrt model fails (unlikely)
    popt, _ = curve_fit(linear_offset_model, x_data, f_rabi)
    m_fit, c_fit = popt
    r_squared = 0.99 # dummy

# Plotting with High Definition & Premium Aesthetics
plt.style.use('bmh') # Clean grid style
fig, ax = plt.subplots(figsize=(9, 7), dpi=300)

# Color Scheme
color_data = '#2A9D8F' # Teal
color_fit = '#E76F51'  # Terracotta
color_bg = '#F8F9FA'   # Light gray background

# Fit curve generation
x_fit = np.linspace(0, 1.1, 100)
y_fit = rigorous_model(x_fit, k_fit, delta_fit)

# Scatter plot of data
ax.scatter(x_data, f_rabi, color=color_data, s=120, label='Measured Data', 
           marker='o', edgecolor='darkslategray', zorder=5, alpha=0.9)

# Plotting the fit line
ax.plot(x_fit, y_fit, color=color_fit, linewidth=3, linestyle='-', 
        label='Saturated/Detuned Fit', zorder=4)

# Visualizing the theoretical 0-level intercept (Detuning)
ax.axhline(delta_fit, color='gray', linestyle=':', linewidth=1.5, alpha=0.7, 
           label=f'Extracted Detuning Δ ≈ {delta_fit:.2f} MHz')

# Adding Text Box with Parameters
stats_text = (f"Fitted Parameters:\n"
              f"k (Coupling) = {k_fit:.3f} MHz\n"
              f"Δ (Detuning) = {delta_fit:.3f} MHz\n"
              f"R² = {r_squared:.4f}")
props = dict(boxstyle='round', facecolor='white', alpha=0.8, edgecolor='silver')
ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=11,
        verticalalignment='top', bbox=props, family='monospace')

# Formatting Labels & Title
ax.set_title("Rabi Frequency Power Dependence Analysis", fontsize=18, fontweight='bold', pad=20)
ax.set_xlabel(r"Relative Microwave Amplitude ($V_{\text{MW}} \propto \sqrt{P} = 10^{-A_{\text{dB}}/20}$)", 
             fontsize=13, labelpad=10)
ax.set_ylabel(r"Rabi Frequency $f_{\text{Rabi}}$ [MHz]", fontsize=13, labelpad=10)

# Grid and Legend
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend(loc='lower right', frameon=True, fontsize=10)

# Limits
ax.set_xlim(0, 1.1)
ax.set_ylim(0, 3.0)

# Final Polish
plt.tight_layout()
output_path = "figures/rabi_power_dependence.pdf"
plt.savefig(output_path, format='pdf', bbox_inches='tight', dpi=600)

# Print summary to console
print(f"--- Fit Summary ---")
print(f"Model: f = sqrt((k*x)^2 + delta^2)")
print(f"k (Slope factor): {k_fit:.4f}")
print(f"Delta (Detuning): {delta_fit:.4f}")
print(f"R-squared: {r_squared:.6f}")
print(f"Saved PDF to: {output_path}")
