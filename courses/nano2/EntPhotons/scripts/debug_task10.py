import numpy as np

K_short = 0.2277  # mV/Hz
tau_short = 230e-9
tau_long = 2.25e-6
K_long = K_short * (tau_long / tau_short)
V_offset = 10.0 # roughly 10mV offset from Task 7

V1 = np.array([0.08, 2, 0.78, 1.1, 3.2, 0.045, 2.1, 3.2, 2.15]) * 1000
V2 = np.array([0.07, 0.13, 0.06, 0.42, 0.65, 0.037, 0.230, 2.75, 1.75]) * 1000
V_joint_meas = np.array([18, 40, 15, 90, 210, 13.5, 57, 700, 340])

# Correct rates by removing offset
r1 = np.maximum(0, V1 - V_offset) / K_short
r2 = np.maximum(0, V2 - V_offset) / K_short

# The average overlap width for two random pulses of width tau is tau/2
# Expected joint voltage = (Rate of overlaps) * (Voltage of average overlap)
# Rate of overlaps = 2 * tau_long * r1 * r2
# Voltage of average overlap = K_long / 2
# Expected joint voltage = (2 * tau_long * r1 * r2) * (K_long / 2) = tau_long * r1 * r2 * K_long
V_joint_exp = tau_long * r1 * r2 * K_long + V_offset

print("Original script formula with offset correction:")
print("Meas: ", V_joint_meas)
print("Exp : ", np.round(V_joint_exp, 1))

# What if the user's original tau_long was exactly what was used for coincidence window?
