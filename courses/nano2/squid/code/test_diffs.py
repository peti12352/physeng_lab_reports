import numpy as np
import shapiro_counter
import scipy.signal

filepath = "task5/task4_shapiro_10ghz_restored.txt"
data = np.loadtxt(filepath, skiprows=1)
length = len(data)
start = 0.1
end = 1 - start
v_sq = data[int(length*start):int(length*end), 1] / 1e3
v_ref = data[int(length*start):int(length*end), 2]
dv = np.gradient(scipy.ndimage.gaussian_filter(v_sq, 5)) / np.gradient(scipy.ndimage.gaussian_filter(v_ref, 5))
dv = scipy.ndimage.gaussian_filter(dv, 3)
peaks, _ = scipy.signal.find_peaks(dv, prominence=np.std(dv)*0.5, distance=10)
v_at_edges = v_sq[peaks]
diffs = np.diff(v_at_edges)
print(f"Diffs: {diffs}")
print(f"Mean Abs Diffs: {np.mean(np.abs(diffs))}")
print(f"Voltage Histogram:")
hist, bin_edges = np.histogram(v_sq, bins=300)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2
hist_smooth = scipy.ndimage.gaussian_filter(hist, sigma=2)
hist_peaks, _ = scipy.signal.find_peaks(hist_smooth, prominence=np.max(hist_smooth)*0.08)
plateaus = bin_centers[hist_peaks]
print(f"Plateau Diffs: {np.diff(plateaus)}")
print(f"Mean Abs Plateau Diffs: {np.mean(np.abs(np.diff(plateaus)))}")
