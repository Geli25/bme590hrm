import scipy.signal as ss
from find_min_max import find_min_max


def find_peak(data):
    min_max = find_min_max(data)
    peaks = ss.find_peaks(data.Voltage, height=min_max, distance=200)
    num_of_beats = peaks[0].__len__()
    print(peaks, num_of_beats)
    peak_data= [peaks, num_of_beats]
    return peak_data
