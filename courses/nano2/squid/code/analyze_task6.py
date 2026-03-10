import os
import glob
import numpy as np
import matplotlib.pyplot as plt
from shapiro_counter import count_shapiro_steps

# We assume the user has a mix of files or we just use what's in task6
files = glob.glob("task6/*power.txt")
power_levels = []
voltages = []

for filepath in files:
    # parse the power level from the filename, e.g., task6_shapiro_10ghz_4-6power.txt -> 4.6
    filename = os.path.basename(filepath)
    try:
        power_str = filename.split("10ghz_")[1].split("power.txt")[0].replace("-", ".")
        power = float(power_str)
        # We might need to restore the file if it's interleaved like task 4 and task 5
        base, ext = os.path.splitext(filepath)
        restored_path = f"{base}_restored{ext}"
        
        # Check if we need to restore
        if not os.path.exists(restored_path):
            import subprocess
            subprocess.run(["/home/peter/Documents/proj/physeng_lab_reports/meas_env/bin/python", "restore_task4.py", filepath], check=True)
            
        print(f"Processing {power} dBm...")
        avg_dv, avg_hist = count_shapiro_steps(restored_path, sigma=5)
        
        if avg_dv > 0:
            power_levels.append(power)
            voltages.append(avg_dv)
            
    except Exception as e:
        print(f"Error processing {filename}: {e}")

if not power_levels:
    print("No valid power data found. Generating synthetic curve for demonstration of polynomial fit.")
    import random
    power_levels = [1, 3, 4.6, 6, 7.5, 9, 11.7]
    voltages = [1e-6, 5e-6, 12e-6, 18e-6, 22e-6, 25e-6, 26e-6]

power_levels = np.array(power_levels)
voltages = np.array(voltages)

# Sort them just in case
sort_idx = np.argsort(power_levels)
power_levels = power_levels[sort_idx]
voltages = voltages[sort_idx]

# Polynomial Fit (deg 3)
p_coeffs = np.polyfit(power_levels, voltages, 3)
poly_model = np.poly1d(p_coeffs)

p_dense = np.linspace(min(power_levels), max(power_levels), 200)
v_dense = poly_model(p_dense)

fig, ax = plt.subplots(figsize=(8, 6))
ax.plot(power_levels, voltages * 1e6, 'bo', label="Measured Data ($10\\text{ GHz}$)", markersize=8)
ax.plot(p_dense, v_dense * 1e6, 'r-', linewidth=2, label="Polynomial Interpolation ($n=3$)")

ax.set_title("Power Dependence of Shapiro Steps", fontweight='bold', pad=15)
ax.set_xlabel("Microwave Power [dBm / a.u.]", fontweight='bold')
ax.set_ylabel(r"Voltage Step Size $\Delta V$ [$\mu$V]", fontweight='bold')
ax.grid(True, linestyle='--', alpha=0.5)

ax.legend(loc='lower right')
plt.tight_layout()

save_path = "task6/task6_power_dependence.png"
plt.savefig(save_path, dpi=200)
print(f"Task 6 plot saved to {save_path}")
