
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Set style
sns.set_theme(style="whitegrid", context="talk")
plt.rcParams['font.family'] = 'sans-serif'

def plot_iv(filename, output_name):
    try:
        # Read the tab-separated file
        # It seems task2.txt has headers
        df = pd.read_csv(filename, sep='\t')
        
        # Check columns
        # Expected: 'Bias Voltage (V)', 'Current (A)'
        if 'Bias Voltage (V)' not in df.columns or 'Current (A)' not in df.columns:
            print(f"Columns not found in {filename}. Columns are: {df.columns}")
            return

        plt.figure(figsize=(10, 6))
        
        # Current in mA for better readability
        plt.plot(df['Bias Voltage (V)'], df['Current (A)'] * 1e3, 
                 linewidth=2, color='#D55E00', label='VO2 Device')
        
        plt.title('VO2 Memristor I-V Characteristic', fontsize=16, fontweight='bold')
        plt.xlabel('Bias Voltage (V)', fontsize=14)
        plt.ylabel('Current (mA)', fontsize=14)
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        plt.legend()
        
        # Annotate Hysteresis
        plt.text(2.5, 0.5, 'Threshold Switching\n(IMT)', fontsize=12, color='#0072B2',
                 horizontalalignment='center')
        
        plt.tight_layout()
        plt.savefig(output_name, dpi=300)
        print(f"Saved {output_name}")
        plt.close()

    except Exception as e:
        print(f"Error plotting IV: {e}")

def plot_oscillator(filename, output_name):
    try:
        # Read the CSV (oscilloscope data)
        # It has a header block, then "index,CH1_Voltage(mV),CH2_Voltage(mV)"
        # We need to skip the metadata lines. "index" is likely around line 11-12.
        # Let's inspect the file structure from the 'head' output earlier.
        # It seems the data starts after the line "Time interval...". 
        
        # We will read with 'header' argument set to the line number where "index" is.
        # Based on previous output: 
        # Line 0: "Channel..."
        # ...
        # Line 9: "Time interval..."
        # Line 10: empty?
        # Line 11: "index,CH1_Voltage(mV),CH2_Voltage(mV)"
        
        # Let's try reading with 'error_bad_lines=False' or skipping rows.
        # We'll try to find the header row dynamically or hardcode 10.
        
        df = pd.read_csv(filename, skiprows=10)
        
        # Check if columns exist
        if 'CH2_Voltage(mV)' not in df.columns:
             # Maybe we missed the header row, try row 11
             df = pd.read_csv(filename, skiprows=11)
        
        if 'CH2_Voltage(mV)' not in df.columns:
             print("Could not find CH2 data in oscillator file.")
             return

        # Create a time axis
        # Time interval is 0.00200uS (micro-seconds) = 2e-9 seconds?
        # Metadata said: "Time interval :,0.00200uS". This is 2 ns.
        dt_us = 0.002
        df['Time (us)'] = df.index * dt_us
        
        plt.figure(figsize=(10, 6))
        plt.plot(df['Time (us)'], df['CH2_Voltage(mV)'], 
                 color='#009E73', linewidth=1.5, label='Output Voltage')
        
        plt.title('Pearson-Anson Oscillator Output', fontsize=16, fontweight='bold')
        plt.xlabel('Time ($\mu$s)', fontsize=14)
        plt.ylabel('Voltage (mV)', fontsize=14)
        plt.grid(True, which='both', linestyle='--', alpha=0.7)
        plt.legend()
        
        plt.tight_layout()
        plt.savefig(output_name, dpi=300)
        print(f"Saved {output_name}")
        plt.close()

    except Exception as e:
        print(f"Error plotting Oscillator: {e}")

if __name__ == "__main__":
    plot_iv('task2.txt', 'docs/task2_iv_HQ.png')
    # switchstayon.csv seems to be the oscillator file based on 'switch' name and scope data
    plot_oscillator('switchstayon.csv', 'docs/task5_oscillator_HQ.png')
