import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit, differential_evolution
from scipy.fft import fft, fftfreq

# Style settings
colors = {
    'primary': '#457B9D',
    'secondary': '#E63946',
    'accent': '#1A936F',
    'background': '#F1FAEE'
}

def rabi_model_complex(t, A, omega, phi, T2eff, beta, B, C):
    """
    User requested model:
    V_R(tau) = A * exp(-(tau / T2eff)**beta) * sin(omega * tau + phi) + B * tau + C
    """
    # Clip parameters to physical ranges for stability
    T2eff = max(T2eff, 1e-3)
    beta = np.clip(beta, 0.1, 5.0)
    return A * np.exp(-(t / T2eff)**beta) * np.sin(omega * t + phi) + B * t + C

def calculate_r_squared(y_data, y_fit):
    residuals = y_data - y_fit
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y_data - np.mean(y_data))**2)
    return 1 - (ss_res / ss_tot)

def fit_and_plot_rabi(f_path, is_colleague=True):
    if not os.path.exists(f_path):
        print(f"File {f_path} not found.")
        return

    # Load data
    if f_path.endswith('.csv'):
        df = pd.read_csv(f_path)
        t_data = df['tau_ns'].values
        y_data = df['R_V'].values * 1000 
    else:
        with open(f_path, 'r') as f:
            header_line = f.readline().strip()
        data = np.loadtxt(f_path)
        t_data = data[:, 0]
        if 'Lockin_X' in header_line and 'Lockin_Y' in header_line:
            y_data = np.sqrt(data[:, 1]**2 + data[:, 2]**2) * 1000
        else:
            y_data = data[:, 1] * 1000

    # Better bounds based on physical expectations (MHz range)
    # omega (rad/ns) -> 1 MHz = 0.006283 rad/ns
    # 0.5 MHz to 15 MHz search range
    omega_min = 2 * np.pi * 0.0001
    omega_max = 2 * np.pi * 0.015 
    
    y_range = np.max(y_data) - np.min(y_data)
    
    # [A, omega, phi, T2eff, beta, B, C]
    lower_bounds = [-y_range * 2, omega_min, -np.pi, 50.0, 0.3, -10.0, np.min(y_data) - y_range]
    upper_bounds = [y_range * 2, omega_max, np.pi, 50000.0, 3.0, 10.0, np.max(y_data) + y_range]

    def objective(p):
        return np.sum((rabi_model_complex(t_data, *p) - y_data)**2)

    print(f"Analyzing {os.path.basename(f_path)} with Physical Bounds...")
    
    # 1. Global optimization in a PHYSICAL range
    res = differential_evolution(objective, list(zip(lower_bounds, upper_bounds)), 
                                  tol=0.005, popsize=20, mutation=(0.5, 1), recombination=0.7)
    p_best = res.x

    # 2. Local refinement
    try:
        popt, _ = curve_fit(rabi_model_complex, t_data, y_data, p0=p_best, 
                            bounds=(lower_bounds, upper_bounds), maxfev=10000)
    except:
        popt = p_best

    y_fitted = rabi_model_complex(t_data, *popt)
    r2 = calculate_r_squared(y_data, y_fitted)

    # Plot
    plt.figure(figsize=(10, 6), dpi=120)
    plt.plot(t_data, y_data, 'o', color=colors['primary'], alpha=0.5, label='Experiment Data', markersize=5)
    
    t_plot = np.linspace(min(t_data), max(t_data), 1000)
    y_plot = rabi_model_complex(t_plot, *popt)
    plt.plot(t_plot, y_plot, '-', color=colors['secondary'], linewidth=2.4, label='Physical Fit ($V_R(\tau)$)')
    
    f_rabi = popt[1] / (2 * np.pi) * 1000 # MHz
    info = (f"$f_{{Rabi}}$ = {f_rabi:.2f} MHz\n"
            f"$T_2^{{eff}}$ = {popt[3]:.1f} ns\n"
            f"$\\beta$ = {popt[4]:.2f}\n"
            f"Contrast = {abs(popt[0]):.2f} mV\n"
            f"$r^2$ = {r2:.4f}")
    
    plt.text(0.97, 0.97, info, transform=plt.gca().transAxes, 
             verticalalignment='top', horizontalalignment='right',
             fontsize=10, bbox=dict(boxstyle='round', facecolor='white', alpha=0.9))

    plt.xlabel(r'$\tau$ (ns)', fontweight='bold')
    plt.ylabel('Signal (mV)', fontweight='bold')
    plt.title('Rabi Oscillations', fontweight='bold', fontsize=14)
    plt.grid(True, ls=':', alpha=0.6)
    plt.legend(loc='lower right')
    plt.tight_layout()
    
    out_dir = 'results/colleague_plots' if is_colleague else 'results'
    os.makedirs(out_dir, exist_ok=True)
    save_name = os.path.basename(f_path).replace('.txt', '.png').replace('.csv', '.png')
    plt.savefig(os.path.join(out_dir, save_name))
    plt.close()
    
    print(f"Success: {os.path.basename(f_path)} | f={f_rabi:.2f} MHz, r2={r2:.4f}")

if __name__ == "__main__":
    # Colleague files
    colleague_files = [
        'colleague_data/rabi_oscillations_task6_6dB_XY.txt',
        'colleague_data/rabi_oscillations_task6_10dB_XY.txt',
        'colleague_data/rabi_oscillations_task6_proper.txt',
        'colleague_data/rabi_oscillations_task6_XY.txt'
    ]
    for f in colleague_files:
        fit_and_plot_rabi(f, is_colleague=True)
        
    # User files
    user_files = [
        'code/time-resolved-odmr/results/Rabi_tau1.csv',
        'code/time-resolved-odmr/results/Rabi_Corrected.csv'
    ]
    for f in user_files:
        fit_and_plot_rabi(f, is_colleague=False)
