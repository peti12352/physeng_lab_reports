import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

docs_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/docs'

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
plt.savefig(os.path.join(docs_dir, 'task9_duty.pdf'))
plt.close()

# --- Task 10 ---
# Calibration factor from Task 6
K = 0.2277  # mV/Hz, assuming same for all channels for now
# Pulse widths
tau_short = 230e-9
tau_long = 2.25e-6

# V in Volts converted to mV for SPAD1, SPAD2
V1 = np.array([0.08, 2, 0.78, 1.1, 3.2, 0.045, 2.1, 3.2, 2.15]) * 1000
V2 = np.array([0.07, 0.13, 0.06, 0.42, 0.65, 0.037, 0.230, 2.75, 1.75]) * 1000
V_joint_meas = np.array([18, 40, 15, 90, 210, 13.5, 57, 700, 340])

# Rates in Hz
r1 = V1 / K
r2 = V2 / K
c_meas = V_joint_meas / K

# Lab note says: "marginal short pulse length setting, coincidence (joint) ling pulse length setting"
# This means the marginals (SPAD1, SPAD2) use short pulse length, but the AND gate is fed these directly?
# If the overlap happens with the pulses coming in, the overlap probability uses the pulse width BEFORE the AND gate, 
# which is the short pulse length (230 ns).
dt = tau_short

c_expected = 2 * dt * r1 * r2
V_joint_expected = c_expected * K

print("Task 10 Analysis:")
print("V_joint_meas (mV):", V_joint_meas)
print("V_joint_exp (mV): ", np.round(V_joint_expected, 1))

plt.figure(figsize=(5, 3))
plt.plot(V_joint_meas, V_joint_expected, 'ko')
plt.plot([0, 800], [0, 800], 'r--')
plt.xlabel('Measured Coincidence (mV)')
plt.ylabel('Expected Coincidence (mV)')
plt.title('Task 10: Random Coincidences')
plt.grid(True, ls=':')
plt.tight_layout()
plt.savefig(os.path.join(docs_dir, 'task10_rand.pdf'))
plt.close()

# --- Re-inspect NewFile1 and NewFile2 ---
# Let's see what the signals actually look like to make a better fig4
for i, filename in enumerate(['NewFile1.csv', 'NewFile2.csv']):
    filepath = os.path.join(docs_dir, filename)
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
        plt.savefig(os.path.join(docs_dir, f'debug_{filename}.pdf'))
        plt.close()
    except Exception as e:
        print(f"Failed {filename}: {e}")

print("Analysis complete.")
