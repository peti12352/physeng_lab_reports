import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter

# Ultra-clean BW Style
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Times New Roman", "DejaVu Serif"],
    "font.size": 9,
    "axes.labelsize": 10,
    "axes.titlesize": 10,
    "xtick.labelsize": 8,
    "ytick.labelsize": 8,
    "legend.fontsize": 8,
    "lines.linewidth": 1.0,
    "figure.dpi": 300,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "grid.alpha": 0.15,
    "grid.linestyle": "--",
    "legend.frameon": False
})

R_BIAS = 10000
DOCS_DIR = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/squid/docs/'
CODE_DIR = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/squid/code/'

def save_refined_plot(data_path, output_name, xlabel, ylabel, mode='iv'):
    try:
        data = np.loadtxt(data_path, skiprows=1)
        v_sq = data[:, 1]
        v_ref = data[:, 2]
        
        fig, ax = plt.subplots(figsize=(4.5, 3.0))
        
        if mode == 'iv':
            # Calculate current in uA
            current = v_ref / R_BIAS * 1e6
            
            # Find the first full cycle (peak to peak)
            # Find index of max current
            idx_max = np.argmax(current)
            idx_min = np.argmin(current)
            
            # Show a range centered around the zero crossing
            # Usually the transition happens near the center
            # We'll take a window that covers the main features
            start = max(0, idx_min - 200)
            end = min(len(current), idx_max + 200)
            
            x = current[start:end]
            y = v_sq[start:end]
            
            # Distinctive marker style for I-V
            ax.plot(x, y, color='black', alpha=0.9, linewidth=0.8, label='Experimental Trace')
            # Add a bit of padding to see the full sharp transition
            ax.set_xlim(min(x)*1.1, max(x)*1.1)
            ax.set_ylim(min(y)*1.1, max(y)*1.1)
            
        elif mode == 'flux':
            # Task 3: Zoom into a few periods to make them visible
            # Total v_ref range is large, let's take a small slice [0, 2]V if possible
            # Or just take indices 1500:2500 which usually covers a good segment
            start, end = 1600, 2600
            x = v_ref[start:end]
            y = v_sq[start:end]
            
            y_smooth = gaussian_filter(y, sigma=5)
            
            # Grayscale scatter with black smooth line
            ax.scatter(x, y, s=5, facecolors='none', edgecolors='#AAAAAA', alpha=0.5, label='Raw Signal')
            ax.plot(x, y_smooth, color='black', linewidth=1.2, label='Smoothed Flux Trace')
            
            ax.set_xlim(min(x), max(x))
            
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend(loc='best')
        plt.tight_layout()
        plt.savefig(DOCS_DIR + output_name)
        plt.close()
        print(f"Plot {output_name} saved successfully.")
        
    except Exception as e:
        print(f"Error in {output_name}: {e}")

# Task 1: Josephson Junction I-V
save_refined_plot(CODE_DIR + '1.txt', 'task1_iv.png', 
                   'Bias Current $I_{\\mathrm{bias}}$ [$\\mu$A]', 'Junction Voltage $V_{\\mathrm{j}}$ [V]', mode='iv')

# Task 2: SQUID I-V
save_refined_plot(CODE_DIR + 'task2.txt', 'task2_iv.png', 
                   'Bias Current $I_{\\mathrm{bias}}$ [$\\mu$A]', 'SQUID Voltage $V_{\\mathrm{sq}}$ [V]', mode='iv')

# Task 3: Flux Response (ZOOMED)
save_refined_plot(CODE_DIR + 'mag.txt', 'task3_flux.png', 
                   'Flux Bias Voltage $V_{\\mathrm{ref}}$ [V]', 'SQUID Voltage $V_{\\mathrm{sq}}$ [V]', mode='flux')
