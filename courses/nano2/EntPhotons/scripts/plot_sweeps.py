import pandas as pd
import matplotlib.pyplot as plt
import os

docs_dir = '/home/peter/Documents/proj/physeng_lab_reports/courses/nano2/EntPhotons/docs'

for i, filename in enumerate(['NewFile1.csv', 'NewFile2.csv']):
    filepath = os.path.join(docs_dir, filename)
    try:
        # Read the csv, skip the first row because it contains 'Time,X(CH1),X(CH2),'
        # the second row contains 'Second,Volt,Volt,'
        # so data starts at row 2.
        df = pd.read_csv(filepath, skiprows=[0], header=0)
        # Rename columns for convenience
        df.columns = ['Time', 'CH1', 'CH2', 'Empty']
        
        plt.figure(figsize=(5, 3))
        plt.plot(df['Time'] * 1e6, df['CH1'], label='CH1', alpha=0.7)
        plt.plot(df['Time'] * 1e6, df['CH2'], label='CH2', alpha=0.7)
        plt.xlabel(r'Time ($\mu$s)')
        plt.ylabel('Voltage (V)')
        pulse_type = 'long' if i == 0 else 'short'
        plt.title(f'Oscilloscope Sweep ({filename})')
        plt.legend()
        plt.tight_layout()
        plt.savefig(os.path.join(docs_dir, f'sweep_{i+1}.pdf'))
        plt.close()
        print(f"Plotted {filename}")
    except Exception as e:
        print(f"Failed {filename}: {e}")
