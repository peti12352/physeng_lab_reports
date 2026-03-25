import numpy as np
import scipy.fft as fft
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

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
            data.append([float(parts[0]), float(parts[2])]) # only take time and fit
    d = np.array(data)
    return d

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

try:
    # 1. Load Measured Spectrum (for comparison)
    sp = read_trt('first_occassion/SPECTRUM10001.trt')
    l_nm_meas = sp[:, 0]
    I_meas = sp[:, 1]
    I_meas -= np.min(I_meas)
    I_meas /= np.max(I_meas)
    
    # 2. Get Pulse duration from Autocorrelation fit
    ac = read_autocorr('first_occassion/autocorr1_61fs_leftpulse_sech2')
    ac[:, 1] -= np.min(ac[:, 1])
    fwhm_ac = calc_fwhm(ac[:, 0], ac[:, 1])
    dt_ps = fwhm_ac / 1.543 # sech2 pulse duration
    
    # 3. Construct Time-Domain Field Envelope E(t)
    # High resolution time grid
    t = np.linspace(-10 * dt_ps, 10 * dt_ps, 8192) # ps
    tau = dt_ps / 1.7627 # tau parameter for sech^2 intensity where fwhm = 1.76 * tau
    
    # Intensity I(t) = sech^2(t/tau)
    I_t = (1.0 / np.cosh(t / tau))**2
    # Field E(t) = sqrt(I(t))
    E_t = np.sqrt(I_t)
    
    # 4. Fourier Transform to get spectral envelope E(nu)
    E_nu = fft.fftshift(fft.fft(fft.ifftshift(E_t)))
    dt = t[1] - t[0] # ps
    nu_THz = fft.fftshift(fft.fftfreq(len(t), dt)) # THz
    
    # Baseband Power Spectrum I(nu) = |E(nu)|^2
    I_nu = np.abs(E_nu)**2
    I_nu /= np.max(I_nu)
    
    # 5. Shift to optical frequency and convert to wavelength
    l_center_nm = l_nm_meas[np.argmax(I_meas)]
    c = 299792458
    nu_center_THz = (c / (l_center_nm * 1e-9)) / 1e12
    
    nu_optical = nu_THz + nu_center_THz
    
    # Convert back to lambda
    l_optical_nm = (c / (nu_optical * 1e12)) * 1e9
    
    # I(lam) = I(nu) * c / lam^2
    I_lam = I_nu * c / (l_optical_nm * 1e-9)**2
    I_lam /= np.max(I_lam)
    
    # Plotting
    plt.figure(figsize=(9, 6))
    plt.plot(l_nm_meas, I_meas, '-', color='gray', alpha=0.7, linewidth=3, label='Measured Spectrometer Data')
    
    # Filter valid wavelength range for plot
    valid = (l_optical_nm > 750) & (l_optical_nm < 830)
    plt.plot(l_optical_nm[valid], I_lam[valid], '-', color='red', linewidth=2, 
             label=f'FTS Derived Spectrum (from {dt_ps*1000:.1f} fs sech$^2$ pulse)')
    
    plt.xlim(740, 840)
    plt.xlabel('Wavelength (nm)', fontsize=12)
    plt.ylabel('Normalized Intensity', fontsize=12)
    plt.title('Fourier Transform Spectroscopy:\nDeriving the Optical Spectrum strictly from the Time-Domain Pulse', fontsize=14)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.savefig('figures/FTS_from_time.pdf', dpi=300)
    print("Successfully generated figures/FTS_from_time.pdf")
except Exception as e:
    print(f"Error occurred: {e}")
