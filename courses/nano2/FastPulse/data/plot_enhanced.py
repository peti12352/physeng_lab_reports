import os
import glob
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def r_squared(y_true, y_pred):
    ss_res = np.sum((y_true - y_pred) ** 2)
    ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
    return 1 - (ss_res / ss_tot) if ss_tot != 0 else 0

def calc_fwhm(x, y):
    half_max = np.max(y) / 2.0
    idx_l = np.where(y >= half_max)[0][0]
    idx_r = np.where(y >= half_max)[0][-1]
    
    if idx_l == 0 or idx_r == len(x) - 1:
        return x[idx_r] - x[idx_l]
        
    x_l = x[idx_l-1] + (x[idx_l] - x[idx_l-1]) * ((half_max - y[idx_l-1]) / (y[idx_l] - y[idx_l-1]))
    x_r = x[idx_r] + (x[idx_r+1] - x[idx_r]) * ((half_max - y[idx_r]) / (y[idx_r+1] - y[idx_r]))
    return x_r - x_l

# 1. Process Spectra
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

# Calculate global df from the initial spectrum
sp1 = read_trt('first_occassion/SPECTRUM10001.trt')
sp1[:, 1] -= np.min(sp1[:, 1])
dl_nm = calc_fwhm(sp1[:, 0], sp1[:, 1])
l_center = sp1[np.argmax(sp1[:, 1]), 0]
c = 299792458
df_Hz = c * (dl_nm * 1e-9) / ((l_center * 1e-9)**2)
df_THz = df_Hz / 1e12
print(f"Calculated spectral bandwidth: {dl_nm:.2f} nm -> {df_THz:.3f} THz at {l_center} nm")

def plot_all_spectra():
    plt.figure(figsize=(10, 6))
    files = [('first_occassion/SPECTRUM10001.trt', 'SPECTRUM10001 (Initial)'), 
             ('first_occassion/SPECTRUM10002.trt', 'SPECTRUM10002'), 
             ('first_occassion/SPECTRUM10003.trt', 'SPECTRUM10003'), 
             ('spektrum_grego_peti.txt', 'spektrum_grego_peti.txt')]
    for fname, lbl in files:
        if 'trt' in fname:
            s = read_trt(fname)
        else:
            s = read_txt_sp(fname)
        if len(s) > 0:
            s[:, 1] -= np.min(s[:, 1])
            plt.plot(s[:, 0], s[:, 1]/np.max(s[:, 1]), label=lbl)

    plt.xlabel('Wavelength (nm)')
    plt.ylabel('Normalized Intensity')
    plt.title('Spectral Profiles')
    plt.xlim(750, 830)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('figures/all_spectra.pdf')
    plt.close()

# 2. Michelson Spectrum
def michelson_spectrum():
    data = np.loadtxt('second_occassion/michelson.txt')
    spectrum = np.sum(data, axis=0) # integrate vertically over interference fringes
    spectrum -= np.min(spectrum)
    
    plt.figure(figsize=(8, 5))
    plt.plot(spectrum, color='purple', linewidth=2)
    plt.xlabel('Horizontal Pixel Index (proportional to Wavelength)')
    plt.ylabel('Integrated Spectral Intensity')
    plt.title('Spectral Profile Extracted from Michelson Interferogram')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('figures/michelson_spectrum.pdf')
    plt.close()

# 3. Autocorrelation Plots with TBP
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
    d = np.array(data)
    # the constant shift (a3) is maintained so curves coincide properly.
    return d

def analyze_and_plot(f_path):
    fname = os.path.basename(f_path)
    d = read_autocorr(f_path)
    if len(d) == 0: return
    
    r2 = r_squared(d[:, 1], d[:, 2])
    fwhm_ac = calc_fwhm(d[:, 0], d[:, 2]) # ps
    
    if 'sech' in fname.lower():
        dt_ps = fwhm_ac / 1.543
        theory = 0.315
        fit_type = 'sech$^2$'
    else:
        dt_ps = fwhm_ac / 1.414
        theory = 0.441
        fit_type = 'Gaussian'
        
    dt_fs = dt_ps * 1000
    tbp = dt_ps * 1e-12 * df_Hz
    
    plt.figure(figsize=(8, 5))
    plt.plot(d[:, 0]*1000, d[:, 1], 'o', markersize=3, label='Raw Data', color='gray', alpha=0.7)
    plt.plot(d[:, 0]*1000, d[:, 2], '-', label=f'{fit_type} Fit ($R^2={r2:.3f}$)', color='red', linewidth=2)
    
    info_text = (f"Fit type: {fit_type}\n"
                 f"$\\Delta t$ = {dt_fs:.1f} fs\n"
                 f"$\\Delta f$ = {df_THz:.2f} THz\n"
                 f"TBP = {tbp:.3f} (Theory limit: {theory})")
    
    plt.text(0.05, 0.95, info_text, transform=plt.gca().transAxes,
             fontsize=11, verticalalignment='top', bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
             
    plt.xlabel('Delay Time (fs)')
    plt.ylabel('Intensity (arb. units)')
    plt.title(f"Autocorrelation: {fname}")
    plt.legend(loc='upper right')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(f"figures/TBP_{fname.replace('+','_')}.pdf")
    plt.close()
    print(f"[{fname}] dt={dt_fs:.1f}fs, TBP={tbp:.3f}, R2={r2:.3f}")

# Execute all
print("Plotting all spectra...")
plot_all_spectra()
print("Plotting Michelson spectrum...")
michelson_spectrum()
print("Analyzing and plotting autocorrelation files...")
for f in glob.glob('first_occassion/autocorr*'):
    analyze_and_plot(f)
print("Done.")
