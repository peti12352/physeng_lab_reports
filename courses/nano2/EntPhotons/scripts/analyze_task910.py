import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/data'
fig_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/figures'
os.makedirs(fig_dir, exist_ok=True)

# --- Task 9 ---
duty = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])
V_duty = np.array([120, 220, 330, 400, 550, 700, 800, 920, 1000])

plt.figure(figsize=(5, 3))
plt.plot(duty, V_duty, 'ko-')
plt.xlabel('Duty Cycle (%)')
plt.ylabel('Coincidence Output (mV)')
plt.title('Task 9: Gated Detection (f = 500 Hz)')
plt.grid(True, ls=':')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'task9_duty.pdf'))
plt.close()

# --- Task 10 ---
# Calibration factor from Task 6
K_short = 0.2277  # mV/Hz
tau_short = 230e-9
tau_long = 2.25e-6
K_long = K_short * (tau_long / tau_short)
V_offset = 10.0 # ~10mV baseline DC offset from analog integrator

V1 = np.array([0.08, 2, 0.78, 1.1, 3.2, 0.045, 2.1, 3.2, 2.15]) * 1000
V2 = np.array([0.07, 0.13, 0.06, 0.42, 0.65, 0.037, 0.230, 2.75, 1.75]) * 1000
V_joint_meas = np.array([18, 40, 15, 90, 210, 13.5, 57, 700, 340])

# Rates in Hz, corrected for DC offset
r1 = np.maximum(0, V1 - V_offset) / K_short
r2 = np.maximum(0, V2 - V_offset) / K_short

# The average overlap width for two random pulses of width tau_long is tau_long / 2.
# Expected joint voltage = (Rate of overlaps) * (Voltage of average overlap)
# Rate of overlaps = 2 * tau_long * r1 * r2
# Voltage of average overlap = K_long / 2
# Expected joint voltage = (2 * tau_long * r1 * r2) * (K_long / 2) = tau_long * r1 * r2 * K_long
V_joint_expected = tau_long * r1 * r2 * K_long + V_offset

print("Task 10 Analysis:")
print("V_joint_meas (mV):", V_joint_meas)
print("V_joint_exp (mV): ", np.round(V_joint_expected, 1))

plt.figure(figsize=(5, 3))
plt.plot(V_joint_meas, V_joint_expected, 'ko')
max_val = max(np.max(V_joint_meas), np.max(V_joint_expected))
plt.plot([0, max_val], [0, max_val], 'r--', label='y = x (Perfect Match)')
plt.xlabel('Measured Coincidence (mV)')
plt.ylabel('Expected Coincidence (mV)')
plt.title('Task 10: Random Coincidences')
plt.legend()
plt.grid(True, ls=':')
plt.tight_layout()
plt.savefig(os.path.join(fig_dir, 'task10_rand.pdf'))
plt.close()

# --- Re-inspect NewFile1 and NewFile2 ---
# Let's see what the signals actually look like to make a better fig4
for i, filename in enumerate(['NewFile1.csv', 'NewFile2.csv']):
    filepath = os.path.join(data_dir, filename)
    try:
        df = pd.read_csv(filepath, skiprows=[0], header=0)
        df.columns = ['Time', 'CH1', 'CH2', 'Empty']
        
        # Check if CH1 or CH2 is a ramp (triangle wave or saw tooth)
        # We can just plot CH1 vs CH2 or Time vs CH
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.plot(df['Time'], df['CH1'], label='CH1')
        plt.plot(df['Time'], df['CH2'], label='CH2')
        plt.legend()
        plt.subplot(1, 2, 2)
        plt.plot(df['CH2'], df['CH1'], 'k.', markersize=1)
        plt.xlabel('CH2')
        plt.ylabel('CH1')
        plt.tight_layout()
        plt.savefig(os.path.join(fig_dir, f'debug_{filename}.pdf'))
        plt.close()
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Analysis complete.")
