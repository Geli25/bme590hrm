import scipy.signal as ss
from find_min_max import find_min_max


def find_peak(data):
    """This function finds the peaks to an ECG data strip.

    Args:
        data(dataframe): A pandas dataframe with a "Voltage" column.

    Returns:
        tuple: A tuple containing:
            peaks(array): Voltages of when a peak is detected.

            beats(int): The number of peaks detected.

    """
    min_max = find_min_max(data)
    peaks = ss.find_peaks(data.Voltage, height=min_max, distance=200)
    num_of_beats = peaks[0].__len__()
    # print(peaks, num_of_beats)
    return peaks, num_of_beats
