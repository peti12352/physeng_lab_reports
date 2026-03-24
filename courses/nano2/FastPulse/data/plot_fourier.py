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
            data.append([float(parts[0]), float(parts[1]), float(parts[2])])
    d = np.array(data)
    d[:, 1] -= np.min(d[:, 1])
    return d

# Load Spectrum
try:
    sp = read_trt('first_occassion/SPECTRUM10001.trt')
    l_nm = sp[:, 0]
    I_l = sp[:, 1]
    I_l -= np.min(I_l)
    
    # Convert to frequency domain
    c = 299792458
    nu_Hz = c / (l_nm * 1e-9)
    nu_THz = nu_Hz / 1e12
    
    # Conserve energy: I(nu) = I(lam) * lam^2 / c
    I_nu = I_l * (l_nm * 1e-9)**2 / c
    
    from scipy.ndimage import gaussian_filter1d
    from scipy.signal import windows

    # Interpolate onto a strictly linear frequency grid
    nu_lin = np.linspace(np.min(nu_THz), np.max(nu_THz), 2048)
    I_nu_lin = np.interp(nu_lin, nu_THz[::-1], I_nu[::-1]) # reverse because freq is reversed
    
    # 1. Smooth the raw spectral data to eliminate hard noise spikes which cause expansive temporal wings
    I_nu_lin = gaussian_filter1d(I_nu_lin, sigma=15)
    
    # 2. Subtract robust baseline and set absolute zero for edges
    baseline = np.median(np.sort(I_nu_lin)[:100]) # approximate baseline from bottom 100 points
    I_nu_lin -= baseline
    I_nu_lin[I_nu_lin < 0] = 0
    I_nu_lin[I_nu_lin < 0.05 * np.max(I_nu_lin)] = 0 # aggressively trim base noise floor
    
    # 3. Apply a slight Tukey window to the array to strictly ensure the edges collapse perfectly matching the zero padding bounds, eliminating Box-Car Sinc ringing
    taper = windows.tukey(len(I_nu_lin), alpha=0.2)
    I_nu_lin *= taper

    # Shift to baseband (DC) to cleanly extract the complex envelope via center of mass instead of random peak
    weights = I_nu_lin / np.sum(I_nu_lin)
    nu_0 = np.sum(nu_lin * weights)
    nu_shifted = nu_lin - nu_0
    
    # Zero pad the spectrum to interpolate/increase the time-domain span and resolution
    pad = 16384
    E_nu = np.sqrt(I_nu_lin) # Flat phase TL assumption
    E_nu_padded = np.pad(E_nu, (pad, pad), mode='constant', constant_values=0)
    
    # Identify the frequency resolution (df)
    d_nu = nu_shifted[1] - nu_shifted[0] # THz
    
    # IFFT to retrieve the time envelope
    E_t = fft.fftshift(fft.ifft(fft.ifftshift(E_nu_padded)))
    t_ps = fft.fftshift(fft.fftfreq(len(E_nu_padded), d_nu)) # Time in ps
    
    # Convert complex field envelope back to Intensity
    I_t = np.abs(E_t)**2
    I_t /= np.max(I_t)
    
    # Calculate transform-limited Intensity Autocorrelation via correlation
    I_ac = np.correlate(I_t, I_t, mode='same')
    I_ac /= np.max(I_ac)
    
    # Load the actually measured initial pulse autocorrelation
    measured = read_autocorr('first_occassion/autocorr1_61fs_leftpulse_sech2')
    t_meas_ps = measured[:, 0]
    # Center the raw measurement time axis physically to t=0
    t_meas_ps -= t_meas_ps[np.argmax(measured[:, 1])]
    I_meas = measured[:, 1]
    
    # Physically scale the Transform-Limited Autocorrelation to overlay perfectly on the raw data baseline boundaries
    baseline_meas = np.min(I_meas)
    peak_meas = np.max(I_meas)
    I_ac_scaled = I_ac * (peak_meas - baseline_meas) + baseline_meas
    
    # Plotting comparison
    plt.figure(figsize=(9, 6))
    plt.plot(t_meas_ps*1000, I_meas, 'o', markersize=4, label='Measured Initial Autocorrelation (61 fs pulse)', color='gray')
    plt.plot(t_ps*1000, I_ac_scaled, '-', label='Transform-Limited Autocorrelation (Derived strictly from Optical Spectrum FFT)', color='blue', linewidth=2.5)
    
    plt.xlim(-200, 200)
    plt.xlabel('Delay Time (fs)', fontsize=12)
    plt.ylabel('Normalized Intensity', fontsize=12)
    plt.title('Fourier Transform Spectroscopy Validation\n(Wiener-Khinchin Theorem & Transform Limit Analysis)', fontsize=14)
    plt.legend(loc='upper right', fontsize=10)
    plt.grid(True, alpha=0.5)
    plt.tight_layout()
    plt.savefig('figures/FT_validation.pdf', dpi=300)
    print("Successfully generated figures/FT_validation.pdf")
except Exception as e:
    print(f"Error occurred: {e}")
