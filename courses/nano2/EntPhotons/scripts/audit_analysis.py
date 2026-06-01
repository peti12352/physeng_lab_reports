import numpy as np
import os
import pandas as pd
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/data'

print("--- TASK 3: FWHM of SPDC Cone ---")
theta = np.array([4, 4.9, 5.5, 6, 6.5, 6.8, 7.2, 7.5, 7.9, 8.3, 9])
counts = np.array([26500, 27000, 30500, 36000, 80050, 156000, 256000, 230000, 178000, 160000, 130000])
baseline = counts[0]
peak = np.max(counts)
half_max = baseline + (peak - baseline) / 2
# Interpolate left and right edges
left_idx = np.where(theta < 7.2)[0]
right_idx = np.where(theta > 7.2)[0]
left_edge = np.interp(half_max, counts[left_idx], theta[left_idx])
# Reverse right side for interp
right_edge = np.interp(half_max, counts[right_idx][::-1], theta[right_idx][::-1])
fwhm_cone = right_edge - left_edge
print(f"Peak at {theta[np.argmax(counts)]} deg")
print(f"FWHM Delta Phi: {fwhm_cone:.2f} deg")

print("\n--- TASK 4: FWHM Jitter ---")
import numpy as np
import os
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

data_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/data'

print("--- TASK 4: FWHM Jitter ---")
t_data = []
events_data = []
try:
    with open(os.path.join(data_dir, 'a.txt'), 'r') as f:
        next(f) # skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                t_str = parts[0].replace(',', '.')
                if 'p' in t_str: t = float(t_str.replace('p', '')) * 1e-12
                elif 'n' in t_str: t = float(t_str.replace('n', '')) * 1e-9
                else: t = float(t_str)
                e = float(parts[1].replace(',', '.'))
                t_data.append(t * 1e9)
                events_data.append(e)
    t = np.array(t_data)
    c = np.array(events_data)
    peak_c = np.max(c)
    hm_c = peak_c / 2
    l_idx = np.where(t < t[np.argmax(c)])[0]
    r_idx = np.where(t > t[np.argmax(c)])[0]
    l_edge = np.interp(hm_c, c[l_idx], t[l_idx])
    r_edge = np.interp(hm_c, c[r_idx][::-1], t[r_idx][::-1])
    fwhm_jitter = r_edge - l_edge
    print(f"FWHM Jitter: {fwhm_jitter*1000:.2f} ps")
except Exception as e:
    print(e)

print("\n--- TASK 6: Linear Calibration Fit ---")
freq = np.array([1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 35, 45, 60, 70, 85, 100, 150, 200, 300, 500, 800, 1400, 2000, 5000, 10000, 15000, 16000, 17000, 20000])
volt = np.array([9.2, 9.4, 9.7, 9.9, 10.0, 10.3, 11.0, 12.3, 13.2, 14.3, 16.6, 18.9, 22.0, 24.6, 28.1, 31.1, 42.2, 53.3, 75.5, 119.7, 186.2, 319.5, 451, 1114, 2221, 3461, 3753, 3873, 3894])

# Fit linear region f in [100, 10000]
mask = (freq >= 100) & (freq <= 10000)
def lin_fit(x, k, b): return k * x + b
popt, _ = curve_fit(lin_fit, freq[mask], volt[mask])
print(f"Calibration K: {popt[0]:.4f} mV/Hz, Offset: {popt[1]:.2f} mV")

print("\n--- TASK 8: Convolution characteristics ---")
delay = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1700, 2000, 2100, 2200, 2300])
V_delay = np.array([1.093, 1.0925, 1.092, 1.092, 1.088, 1.084, 1.079, 1.074, 1.069, 1.063, 1.059, 1.034, 1.011, 0.988, 0.965, 0.919, 0.872, 0.823, 0.772, 0.722, 0.675, 0.629, 0.538, 0.436, 0.292, 0.152, 0.0968, 0.044, 0.008])

max_V = np.max(V_delay)
idx_start_fall = np.where(V_delay < max_V - 0.01)[0][0]
idx_end_fall = np.where(V_delay < 0.01)[0][-1]
print(f"Shortest noticeable delay: {delay[idx_start_fall]} ns")
print(f"Longest measurable delay: {delay[idx_end_fall]} ns")
