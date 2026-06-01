import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import os

os.makedirs('docs/plots', exist_ok=True)

windows = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 80, 100, 120, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900, 1000, 1500, 2500])
counts = np.array([14, 35, 130, 150, 190, 190, 205, 215, 225, 230, 240, 240, 275, 295, 340, 360, 385, 420, 435, 470, 485, 520, 620, 710, 790, 960, 1150, 1400, 1600, 1820, 2110, 2520, 3000, 3500, 4000, 4350, 4750, 6800, 11000])

# Piecewise linear fit
def piecewise_linear(x, x0, y0, k):
    return np.piecewise(x, [x < x0, x >= x0],
                        [lambda x: y0, 
                         lambda x: y0 + k * (x - x0)])

# Initial guess: break around 50, plateau around 450, slope (11000-470)/(2500-50) ~ 4.3
p0 = [50, 450, 4.3]

try:
    popt, pcov = curve_fit(piecewise_linear, windows, counts, p0=p0, bounds=([1, 0, 0], [1000, 2000, 20]))
    x0, y0, k = popt
except Exception as e:
    print(f"Fit failed: {e}")
    x0, y0, k = 50, 470, 4.3 # fallback

# For a better visualization, we might want to plot the log scale or limit the axes.
# Since it goes from 1 to 2500, log scale on x is good.
plt.figure(figsize=(8, 5))
plt.plot(windows, counts, 'ko', markersize=5, label='Measured Data')

# Generate smooth line for fit
x_fit = np.linspace(1, 2500, 1000)
plt.plot(x_fit, piecewise_linear(x_fit, x0, y0, k), 'r-', linewidth=2, 
         label=f'Piecewise Fit\nBreakpoint: {x0:.1f}\nSlope: {k:.2f} cps/unit')

plt.axvline(x0, color='blue', linestyle='--', alpha=0.6)

plt.xscale('log')
plt.title('Task 5: Coincidence Rate vs. Window Width', fontsize=14)
plt.xlabel('Coincidence Window Width (arb. units)', fontsize=12)
plt.ylabel('Coincidence Count Rate (cps)', fontsize=12)
plt.grid(True, which="both", ls="--", alpha=0.5)
plt.legend(fontsize=10)
plt.tight_layout()
plt.savefig('figures/task5_window.pdf')
plt.close()

print(f"Task 5 plot generated. Breakpoint at {x0:.2f}, Slope: {k:.3f}")
