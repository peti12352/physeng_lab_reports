import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
from scipy.stats import linregress

docs_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/docs'

f = np.array([1, 2, 3, 4, 5, 7, 10, 15, 20, 25, 35, 45, 60, 70, 85, 100, 150, 200, 300, 500, 800, 1400, 2000, 5000, 10000, 15000, 16000, 17000, 20000])
V = np.array([9.2, 9.4, 9.7, 9.9, 10.0, 10.3, 11.0, 12.3, 13.2, 14.3, 16.6, 18.9, 22.0, 24.6, 28.1, 31.1, 42.2, 53.3, 75.5, 119.7, 186.2, 319.5, 451, 1114, 2221, 3461, 3753, 3873, 3894])

# Linear region, let's say from f=100 to f=15000
mask = (f >= 100) & (f <= 15000)
res = linregress(f[mask], V[mask])
print(f"Task 6 Calibration Factor (Slope): {res.slope:.4f} mV/Hz")
print(f"Task 6 Intercept: {res.intercept:.4f} mV")

for i, filename in enumerate(['NewFile3.csv', 'NewFile4.csv', 'NewFile5.csv', 'NewFile6.csv']):
    filepath = os.path.join(docs_dir, filename)
    try:
        df = pd.read_csv(filepath, skiprows=[0], header=0)
        df.columns = ['Time', 'CH1', 'CH2', 'Empty']
        
        plt.figure(figsize=(5, 3))
        plt.plot(df['Time'], df['CH1'], label='CH1', alpha=0.7)
        plt.plot(df['Time'], df['CH2'], label='CH2', alpha=0.7)
        plt.xlabel(r'Time (s)')
        plt.ylabel('Voltage (V)')
        plt.title(f'Oscilloscope ({filename})')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(docs_dir, f'plot_{filename.split(".")[0]}.pdf'))
        plt.close()
        print(f"Plotted {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")
