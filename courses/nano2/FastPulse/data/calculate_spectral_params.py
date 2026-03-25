import numpy as np
import os

def calc_fwhm(x, y):
    y_shifted = y - np.min(y)
    half_max = np.max(y_shifted) / 2.0
    idx_l = np.where(y_shifted >= half_max)[0][0]
    idx_r = np.where(y_shifted >= half_max)[0][-1]
    
    if idx_l == 0 or idx_r == len(x) - 1:
        return x[idx_r] - x[idx_l]
        
    x_l = x[idx_l-1] + (x[idx_l] - x[idx_l-1]) * ((half_max - y_shifted[idx_l-1]) / (y_shifted[idx_l] - y_shifted[idx_l-1]))
    x_r = x[idx_r] + (x[idx_r+1] - x[idx_r]) * ((half_max - y_shifted[idx_r]) / (y_shifted[idx_r+1] - y_shifted[idx_r]))
    return x_r - x_l

def read_trt(f):
    data = []
    with open(f, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('Wave') and not line.startswith('0') and not line.startswith('['):
                try:
                    parts = line.split(';')
                    data.append([float(parts[0]), float(parts[1])])
                except:
                    pass
    return np.array(data)

def read_txt_sp(f):
    data = []
    start = False
    with open(f, 'r') as file:
        for line in file:
            if line.startswith('>>>>>Begin Spectral Data<<<<<'):
                start = True
                continue
            if start and line.strip():
                parts = line.replace(',', '.').split('\t')
                try:
                    data.append([float(parts[0]), float(parts[1])])
                except:
                    pass
    return np.array(data)

files = [
    'first_occassion/SPECTRUM10001.trt',
    'first_occassion/SPECTRUM10002.trt',
    'first_occassion/SPECTRUM10003.trt',
    'spektrum_grego_peti.txt'
]

c = 299792458

print("-" * 80)
for f in files:
    if not os.path.exists(f):
        print(f"File not found: {f}")
        continue
        
    if f.endswith('.trt'):
        sp = read_trt(f)
    else:
        sp = read_txt_sp(f)
        
    if len(sp) == 0:
        print(f"No data in {f}")
        continue
        
    sp[:, 1] -= np.min(sp[:, 1])
    dl_nm = calc_fwhm(sp[:, 0], sp[:, 1])
    peak_idx = np.argmax(sp[:, 1])
    l_center = sp[peak_idx, 0]
    
    # Calculate limits
    hm = np.max(sp[:, 1]) / 2.0
    # Left limit
    l1_idx = np.where(sp[0:peak_idx, 1] <= hm)[0]
    l1 = sp[l1_idx[-1], 0] if len(l1_idx) > 0 else sp[0, 0]
    # Right limit
    l2_idx = np.where(sp[peak_idx:, 1] <= hm)[0]
    l2 = sp[peak_idx + l2_idx[0], 0] if len(l2_idx) > 0 else sp[-1, 0]

    df_Hz = c * (dl_nm * 1e-9) / ((l_center * 1e-9)**2)
    df_THz = df_Hz / 1e12
    
    print(f"File: {f}")
    print(f"  Peak Wavelength: {l_center:.2f} nm")
    print(f"  FWHM Bandwidth:  {dl_nm:.2f} nm (from {l1:.1f} to {l2:.1f} nm)")
    print(f"  Freq Bandwidth:  {df_THz:.3f} THz")
    print("-" * 80)
