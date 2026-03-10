import numpy as np
from scipy.stats import linregress

freqs_ghz = [8, 9, 9.5, 10, 11, 12]
v_uv = [18, 20, 21, 23, 26, 24] # example values
f_hz = np.array(freqs_ghz) * 1e9
v_v = np.array(v_uv) * 1e-6

print(linregress(f_hz, v_v))
