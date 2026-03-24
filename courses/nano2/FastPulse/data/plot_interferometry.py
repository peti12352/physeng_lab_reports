import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

def plot_interferogram():
    try:
        # The file contains space separated integers representing a 2D image array
        data = np.loadtxt('second_occassion/michelson.txt') # michelson.txt is a large 2D text matrix
        
        plt.figure(figsize=(10, 6))
        # Plotting the 2D array as an image
        # Using a proper colormap for interferograms (gray or viridis work well)
        plt.imshow(data, aspect='auto', cmap='inferno')
        plt.colorbar(label='Intensity (counts)')
        plt.xlabel('Horizontal Pixels (Wavelength Axis)')
        plt.ylabel('Vertical Pixels (Spatial Axis)')
        plt.title('Spectrally Resolved Interferogram (Michelson)')
        plt.tight_layout()
        plt.savefig('figures/michelson_interferogram.pdf', dpi=300)
        plt.close()
        print("Successfully created michelson_interferogram.pdf")
        
    except Exception as e:
        print(f"Failed to plot interferogram: {e}")

if __name__ == "__main__":
    plot_interferogram()
