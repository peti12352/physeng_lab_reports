import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

docs_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/docs'

K_short = 0.2277  # mV/Hz
tau_short = 230e-9
tau_long = 2.25e-6

K_long = K_short * (tau_long / tau_short)

V1 = np.array([0.08, 2, 0.78, 1.1, 3.2, 0.045, 2.1, 3.2, 2.15]) * 1000
V2 = np.array([0.07, 0.13, 0.06, 0.42, 0.65, 0.037, 0.230, 2.75, 1.75]) * 1000
V_joint_meas = np.array([18, 40, 15, 90, 210, 13.5, 57, 700, 340])

r1 = V1 / K_short
r2 = V2 / K_short

# From the manual: P(overlap) = \Delta t * r2
# Expected rate equivalent = \Delta t * r1 * r2
c_expected = tau_long * r1 * r2
V_joint_expected = c_expected * K_long

print("V_joint_meas (mV):", V_joint_meas)
print("V_joint_exp (mV): ", np.round(V_joint_expected, 1))

plt.figure(figsize=(5, 3))
plt.plot(V_joint_meas, V_joint_expected, 'ko')
max_val = max(np.max(V_joint_meas), np.max(V_joint_expected))
plt.plot([0, max_val], [0, max_val], 'r--', label='y = x (Perfect Match)')
plt.xlabel('Measured Coincidence (mV)')
plt.ylabel('Theoretical Coincidence (mV)')
plt.title('Task 10: Random Coincidences')
plt.legend()
plt.grid(True, ls=':')
plt.tight_layout()
plt.savefig(os.path.join(docs_dir, 'task10_rand.pdf'))
plt.close()
