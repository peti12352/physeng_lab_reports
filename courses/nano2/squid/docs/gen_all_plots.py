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

def save_refined_plot(data_path, output_name, xlabel, ylabel, mode='iv', yscale=1.0):
    try:
        data = np.loadtxt(data_path, skiprows=1)
        v_sq = data[:, 1]
        v_ref = data[:, 2]
        
        # Determine points per cycle
        with open(data_path, 'r') as f:
            header = f.readline()
        match = re.search(r'num\. of cycles: (\d+)', header)
        num_cycles = int(match.group(1)) if match else 1
        pts_per_cycle = len(data) // num_cycles
        
        fig, ax = plt.subplots(figsize=(4.5, 3.0))
        
        if mode == 'iv':
            # Use just the first cycle for a clean trace
            start, end = 0, pts_per_cycle
            current = v_ref[start:end] / R_BIAS * 1e6 # uA
            y = v_sq[start:end] * yscale
            
            ax.plot(current, y, color='black', alpha=0.9, linewidth=1.0, label='Experimental Trace')
            
            # Auto-range logic
            ax.set_xlim(np.min(current)*1.1, np.max(current)*1.1)
            ax.set_ylim(np.min(y) - 0.1*(np.max(y)-np.min(y)), np.max(y) + 0.1*(np.max(y)-np.min(y)))
            
        elif mode == 'flux':
            # Take a small segment (e.g. half a cycle or two periods)
            # 1520 points is usually one triangle sweep
            start, end = 0, pts_per_cycle
            x = v_ref[start:end]
            y = v_sq[start:end] * yscale
            
            y_smooth = gaussian_filter(y, sigma=5)
            
            ax.scatter(x, y, s=5, facecolors='none', edgecolors='#AAAAAA', alpha=0.5, label='Raw Signal')
            ax.plot(x, y_smooth, color='black', linewidth=1.2, label='Smoothed Flux Trace')
            
            ax.set_xlim(np.min(x), np.max(x))
            
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.legend(loc='best')
        plt.tight_layout()
        plt.savefig(DOCS_DIR + output_name)
        plt.close()
        print(f"Plot {output_name} saved.")
        
    except Exception as e:
        print(f"Error in {output_name}: {e}")

import re # Need re
# Task 1: Josephson Junction I-V
save_refined_plot(CODE_DIR + 'task1/1.txt', 'task1_iv.png', 
                   'Bias Current $I_{\\mathrm{bias}}$ [$\\mu$A]', 'Junction Voltage $V_{\\mathrm{j}}$ [mV]', mode='iv')

# Task 2: SQUID I-V
save_refined_plot(CODE_DIR + 'task2/task2.txt', 'task2_iv.png', 
                   'Bias Current $I_{\\mathrm{bias}}$ [$\\mu$A]', 'SQUID Voltage $V_{\\mathrm{SQUID}}$ [$\\mu$V]', mode='iv', yscale=1e6/1000)

# Task 3: Flux Response (ZOOMED)
save_refined_plot(CODE_DIR + 'task3/mag.txt', 'task3_flux.png', 
                   'Flux Bias Voltage $V_{\\mathrm{ref}}$ [V]', 'SQUID Voltage $V_{\\mathrm{SQUID}}$ [$\\mu$V]', mode='flux', yscale=1e6/1000)
