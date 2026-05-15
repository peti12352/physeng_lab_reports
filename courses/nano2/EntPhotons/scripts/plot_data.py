import matplotlib.pyplot as plt
import numpy as np
import os

docs_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/docs'

# Task 4: Start-Stop Histogram from a.txt
# t (s) - HBT Measurement    Start-Stop Historam (events per second) - HBT Measurement
t_data = []
events_data = []
try:
    with open(os.path.join(docs_dir, 'a.txt'), 'r') as f:
        next(f) # skip header
        for line in f:
            parts = line.strip().split('\t')
            if len(parts) == 2:
                # Convert time string with unit prefixes to float
                t_str = parts[0].replace(',', '.')
                if 'p' in t_str:
                    t = float(t_str.replace('p', '')) * 1e-12
                elif 'n' in t_str:
                    t = float(t_str.replace('n', '')) * 1e-9
                else:
                    t = float(t_str)
                e = float(parts[1].replace(',', '.'))
                t_data.append(t * 1e9) # plot in ns
                events_data.append(e)

    plt.figure(figsize=(5, 3))
    plt.plot(t_data, events_data, 'k.-', markersize=3, linewidth=1)
    plt.xlabel('Time (ns)')
    plt.ylabel('Events per second')
    plt.title('Start-Stop Histogram (HBT)')
    plt.tight_layout()
    plt.savefig(os.path.join(docs_dir, 'task4_hist.pdf'))
    plt.close()
except Exception as e:
    print(f"Error Task 4: {e}")

# Task 7
try:
    f = [1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 35, 45, 60, 70, 85, 100, 150, 200, 300, 500, 800, 1400, 2000, 5000, 10000, 15000, 16000, 17000, 20000]
    V = [9.2, 9.4, 9.7, 9.9, 10.0, 10.3, 11.0, 12.3, 13.2, 14.3, 16.6, 18.9, 22.0, 24.6, 28.1, 31.1, 42.2, 53.3, 75.5, 119.7, 186.2, 319.5, 451, 1114, 2221, 3461, 3753, 3873, 3894]
    
    plt.figure(figsize=(5, 3))
    plt.loglog(f, V, 'k.-', markersize=4, linewidth=1)
    plt.xlabel('Pulse Frequency (Hz)')
    plt.ylabel('Analog Output Voltage (mV)')
    plt.title('Counter Calibration (230ns pulse)')
    plt.grid(True, which="both", ls=":", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(docs_dir, 'task7_freq.pdf'))
    plt.close()
except Exception as e:
    print(f"Error Task 7: {e}")

# Task 8
try:
    delay = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000, 1200, 1400, 1700, 2000, 2100, 2200, 2300]
    V_delay = [1.093, 1.0925, 1.092, 1.092, 1.088, 1.084, 1.079, 1.074, 1.069, 1.063, 1.059, 1.034, 1.011, 0.988, 0.965, 0.919, 0.872, 0.823, 0.772, 0.722, 0.675, 0.629, 0.538, 0.436, 0.292, 0.152, 0.0968, 0.044, 0.008]
    
    plt.figure(figsize=(5, 3))
    plt.plot(delay, V_delay, 'k.-', markersize=4, linewidth=1)
    plt.xlabel('Time Delay (ns)')
    plt.ylabel('Coincidence Output (V)')
    plt.title(r'Time Delay Effect ($\Delta t = 2.25 \mu s$)')
    plt.grid(True, ls=":", alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(docs_dir, 'task8_delay.pdf'))
    plt.close()
except Exception as e:
    print(f"Error Task 8: {e}")
print("Plots generated successfully.")
