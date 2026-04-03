import os
import glob
import numpy as np
import matplotlib.pyplot as plt

def read_autocorr(f):
    with open(f, 'r') as file:
        lines = file.readlines()
    
    start_idx = 0
    for i, line in enumerate(lines):
        if line.startswith('time\tacf1\tfit'):
            start_idx = i + 2
            break
    
    data = []
    for line in lines[start_idx:]:
        if line.strip():
            parts = line.split()
            data.append([float(parts[0]), float(parts[1]), float(parts[2])])
    return np.array(data)

def plot_autocorr_comparison(left_file, right_file, fit_type, out_name, title):
    data_l = read_autocorr(left_file)
    data_r = read_autocorr(right_file)
    
    plt.figure(figsize=(8, 5))
    plt.plot(data_l[:, 0], data_l[:, 1], 'o', markersize=2, label='Left (Raw Data)', color='blue')
    plt.plot(data_l[:, 0], data_l[:, 2], '-', label=f'Left ({fit_type} Fit)', color='navy')
    
    plt.plot(data_r[:, 0], data_r[:, 1], 'o', markersize=2, label='Right (Raw Data)', color='orange')
    plt.plot(data_r[:, 0], data_r[:, 2], '-', label=f'Right ({fit_type} Fit)', color='darkorange')
    
    plt.xlabel('Delay Time (ps)')
    plt.ylabel('Intensity (arb. units)')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'figures/{out_name}.pdf')
    plt.close()

plot_autocorr_comparison('first_occassion/autocorr1_61fs_leftpulse_sech2', 'first_occassion/autocorr1_119fs_rightpulse_sech2', 'sech$^2$', 'comp_left_right_sech2', '1cm Glass Dispersion (Left vs Right) - sech$^2$ Fit')
plot_autocorr_comparison('first_occassion/autocorr1_68fs_leftpulse_gauss', 'first_occassion/autocorr1_138fs_rightpulse_gauss', 'Gaussian', 'comp_left_right_gauss', '1cm Glass Dispersion (Left vs Right) - Gaussian Fit')

def plot_multi(files, labels, out_name, title):
    plt.figure(figsize=(10, 6))
    colors = plt.cm.viridis(np.linspace(0, 0.9, len(files)))
    for f, lbl, color in zip(files, labels, colors):
        d = read_autocorr(f)
        # Normalize to maximum 1 for better visual comparison of shapes
        d[:, 2] = d[:, 2] / np.max(d[:, 2])
        # Center the time array around the peak to overlay them perfectly
        peak_idx = np.argmax(d[:, 2])
        time_centered = d[:, 0] - d[peak_idx, 0]
        
        plt.plot(time_centered, d[:, 2], '-', label=lbl, color=color)

    plt.xlabel('Delay Time (ps)')
    plt.ylabel('Normalized Intensity')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f'figures/{out_name}.pdf')
    plt.close()

files_sech2 = [
    'first_occassion/autocorr1_61fs_leftpulse_sech2',
    'first_occassion/autocorr_comp_884fs_sech2',
    'first_occassion/autocorr_comp+glasscube_847fs_sech2',
    'first_occassion/autocorr_comp+TeO2_240fs_sech2',
    'first_occassion/autocorr_comp+TeO2_extended_65fs_sech2',
    'first_occassion/autocorr_comp+shifted_prism+TeO2+glass_64fs_sech2'
]
labels_sech2 = [
    'Initial (61 fs)',
    'Compressor (884 fs)',
    '+ Glass Cube (847 fs)',
    '+ 3cm TeO2 (240 fs)',
    '+ 4cm TeO2 (65 fs)',
    'Shifted Prism (64 fs)'
]
plot_multi(files_sech2, labels_sech2, 'comp_all_sech2', 'Pulse Compression Evolution (sech$^2$ Fits - Normalized & Centered)')

# Spectra Plots
def read_trt(f):
    data = []
    with open(f, 'r') as file:
        for line in file:
            if line.strip() and not line.startswith('Wave') and not line.startswith('0') and not line.startswith('I') and not line.startswith('A') and not line.startswith('N') and not line.startswith('D') and not line.startswith('T') and not line.startswith('['):
                try:
                    parts = line.split(';')
                    data.append([float(parts[0]), float(parts[1])])
                except:
                    pass
    return np.array(data)

def read_txt(f):
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

sp1 = read_trt('first_occassion/SPECTRUM10001.trt')
sp3 = read_txt('spektrum_grego_peti.txt')

sp1_norm = sp1[:, 1] / np.max(sp1[:, 1])
sp3_norm = sp3[:, 1] / np.max(sp3[:, 1])

plt.figure(figsize=(10, 6))
plt.plot(sp1[:, 0], sp1_norm, label='SPECTRUM10001 (Initial)')
plt.plot(sp3[:, 0], sp3_norm, label='spektrum_grego_peti.txt (After comp + samples)')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Normalized Intensity')
plt.title('Spectral Profiles')
plt.legend()
plt.grid(True)
plt.xlim(750, 820)
plt.tight_layout()
plt.savefig('figures/spectra.pdf')
plt.close()

print("Plotting complete.")
