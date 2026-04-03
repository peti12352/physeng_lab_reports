import numpy as np
import re
import os
import sys

def restore_screen_data(filename):
    # Read header
    with open(filename, "r") as f:
        header = f.readline().strip()

    # Get num of cycles
    match = re.search(r"num\. of cycles:\s*(\d+)", header)
    if not match:
        # Fallback if the header is slightly different or missing the info
        print(f"Warning: Could not find number of cycles in header for {filename}. Assuming 1.")
        num_of_cycles = 1
    else:
        num_of_cycles = int(match.group(1))

    # Load data without header
    # Some files might use commas, but SQUID data usually uses tabs
    try:
        data = np.loadtxt(filename, skiprows=1)
    except Exception:
        data = np.loadtxt(filename, skiprows=1, delimiter="\t")

    total_rows = data.shape[0]
    if total_rows % num_of_cycles != 0:
        raise ValueError(f"Number of rows ({total_rows}) not divisible by num_of_cycles ({num_of_cycles})")

    M = total_rows // num_of_cycles
    
    # Reshape to 3D: (cycles, 3 columns, M points per channel)
    # The assumes original data was one long sequence: [all_T, all_CH1, all_CH2]
    # but was loaded into N x 3 rows by mistake.
    restored_3d = data.reshape(num_of_cycles, 3, M)

    # Save as column stack (T, CH1, CH2) for each cycle concatenated
    stacked_cycles = [
        np.column_stack((restored_3d[i, 0], restored_3d[i, 1], restored_3d[i, 2]))
        for i in range(num_of_cycles)
    ]
    final_data = np.vstack(stacked_cycles)

    base, ext = os.path.splitext(filename)
    new_filename = base + "_restored" + ext

    header_out = f"time[s]\tCH1[V]\tCH2[V] (num. of cycles: {num_of_cycles})"
    np.savetxt(
        new_filename,
        final_data,
        delimiter="\t",
        header=header_out,
        comments=""
    )
    print(f"Successfully restored data to: {new_filename}")
    return new_filename

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python restore_task4.py <filename1> <filename2> ...")
    else:
        for f in sys.argv[1:]:
            try:
                restore_screen_data(f)
            except Exception as e:
                print(f"Error restoring {f}: {e}")
