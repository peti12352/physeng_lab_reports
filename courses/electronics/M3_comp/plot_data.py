import pandas as pd
import matplotlib.pyplot as plt
import os

def plot_hysteresis(csv_file='data4.csv', output_image='plot4.png'):
    """
    Loads comparator data from a CSV file and plots the hysteresis curve.

    The CSV file must contain the following columns:
    - U_in_increase: Driving voltage while increasing.
    - U_out_increase: Output voltage while increasing.
    - U_in_decrease: Driving voltage while decreasing.
    - U_out_decrease: Output voltage while decreasing.

    Args:
        csv_file (str): The path to the input CSV file.
        output_image (str): The path to save the output plot image.
    """
    if not os.path.exists(csv_file):
        print(f"Error: The file '{csv_file}' was not found.")
        return

    # Load the data from the CSV file
    try:
        data = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Error reading CSV file: {e}")
        return

    # Create a new figure and axes for the plot
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(10, 6))

    # Plot the data for increasing input voltage
    ax.plot(data['U_in_increase'], data['U_out_increase'], 'o-', label='Increasing Input', color='royalblue')

    # Plot the data for decreasing input voltage
    ax.plot(data['U_in_decrease'], data['U_out_decrease'], 's--', label='Decreasing Input', color='darkorange')

    # Set the labels for the axes with units
    ax.set_xlabel('Driving Voltage (V)', fontsize=12)
    ax.set_ylabel('Output Voltage (V)', fontsize=12)

    # Set the title of the plot
    ax.set_title('Comparator Hysteresis Curve', fontsize=14, fontweight='bold')

    # Add a legend to distinguish the lines
    ax.legend(fontsize=10)

    # Improve tick label appearance
    ax.tick_params(axis='both', which='major', labelsize=10)

    # Save the figure to a file
    try:
        fig.savefig(output_image, dpi=300, bbox_inches='tight')
        print(f"Plot successfully saved to '{output_image}'")
    except Exception as e:
        print(f"Error saving plot: {e}")

if __name__ == '__main__':
    plot_hysteresis()
