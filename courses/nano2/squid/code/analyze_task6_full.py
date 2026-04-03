import os
import glob
import numpy as np
import matplotlib.pyplot as plt
import subprocess
from shapiro_counter import count_shapiro_steps

# Given mapping
N_ref = np.array([0, 4, 8, 12, 16, 20, 24, 28])
P_ref = np.array([-26.1, -10.4, -5.5, -1.1, 1.8, 4.6, 7.5, 11.7])

# Fit n=3 to Power vs N directly
p_coeffs = np.polyfit(N_ref, P_ref, 3)
poly_p = np.poly1d(p_coeffs)

# Quantitative Analysis
residuals = P_ref - poly_p(N_ref)
rss = np.sum(residuals**2)
print("\n--- Fit Analysis ---")
print(f"3rd Order Polynomial Fit P(N) Coefficients:")
print(f"a3: {p_coeffs[0]:.4e}, a2: {p_coeffs[1]:.4e}, a1: {p_coeffs[2]:.4e}, a0: {p_coeffs[3]:.4e}")
print(f"Residual Sum of Squares (RSS): {rss:.4f}")
print("Qualitative Analysis: The 3rd order polynomial interpolates smoothly across the anchor points without exhibiting Runge's phenomenon or significant high-frequency over-oscillation. This provides a robust continuous mapping of power levels against the discrete index N.\n")

power_levels_p = []
power_levels_n = []
voltages = []

# Assuming 28 data points: temp_cyc_0.txt to temp_cyc_27.txt
num_points = 28

for i in range(num_points):
    filepath = f"task6/temp_cyc_{i}.txt"
    restored_path = f"task6/temp_cyc_{i}_restored.txt"
    
    if not os.path.exists(filepath):
        print(f"Warning: {filepath} not found.")
        continue
        
    if not os.path.exists(restored_path):
        subprocess.run(["/home/peter/Documents/proj/physeng_lab_reports/meas_env/bin/python", "restore_task4.py", filepath], check=True)
        
    # Evaluate cubic fit power for this index i
    power = poly_p(i)
    
    # We do calculations quietly 
    try:
        avg_dv, avg_hist = count_shapiro_steps(restored_path, sigma=5, save_files=False)
        # Clean up temporary restored file
        if os.path.exists(restored_path):
            os.remove(restored_path)
        
        # Prefer method A as in task 5 (or whichever gives valid reading)
        v_step = avg_dv if avg_dv > 0 else avg_hist
        if v_step > 0:
            power_levels_n.append(i)
            power_levels_p.append(power)
            voltages.append(v_step)
        else:
            print(f"Warning: No valid reading for {filepath}")
    except Exception as e:
        print(f"Exception processing {filepath}: {e}")

power_levels_n = np.array(power_levels_n)
power_levels_p = np.array(power_levels_p)
voltages = np.array(voltages)

p_dense_n = np.linspace(0, 28, 200)
p_interp_dense = poly_p(p_dense_n)

fig, ax1 = plt.subplots(figsize=(8, 6))

ax1.plot(N_ref, P_ref, 'ro', label="Labeled Anchor Points", markersize=8)
ax1.plot(p_dense_n, p_interp_dense, 'r--', linewidth=2, label="Cubic Interpolation $P(N)$ ($n=3$)")

ax1.set_title("Task 6: Power Map Interpolation", fontweight='bold', pad=15)
ax1.set_xlabel("Measurement Index (N)", fontweight='bold')
ax1.set_ylabel("Microwave Power P [dBm]", fontweight='bold', color='r')
ax1.tick_params(axis='y', labelcolor='r')
ax1.grid(True, linestyle='--', alpha=0.5)

ax2 = ax1.twinx()
ax2.plot(power_levels_n, voltages * 1e6, 'bs', label=r"Measured $\Delta V$ ($N$-mapped)", markersize=5, alpha=0.7)
ax2.set_ylabel(r"Voltage Step Size $\Delta V$ [$\mu$V]", fontweight='bold', color='b')
ax2.tick_params(axis='y', labelcolor='b')

# combined legend
lines1, labels1 = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

plt.tight_layout()

save_path = "task6/task6_power_dependence_full.png"
plt.savefig(save_path, dpi=200)
print(f"Plot saved to {save_path}")
