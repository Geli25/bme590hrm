from readData import import_data
from validateData import validate
from find_min_max import find_min_max
from find_peak import find_peak
from get_duration import get_duration
from get_beat_times import get_beat_times
from calculate_mean_bpm import calculate_mean_bpm


def create_dictionary(directory):
    data = validate(import_data(directory))
    min_max = find_min_max(data)
    duration = get_duration(data)
    peaks = find_peak(data)
    beats = get_beat_times(peaks, data)
    mean_bpm = calculate_mean_bpm(data, beats)

    metrics = {
        "mean_hr_bpm": mean_bpm,
        "voltage_extremes": min_max,
        "duration": duration,
        "num_beats": peaks[1],
        "beats": beats
    }

    print(metrics)
    return metrics


if __name__ == '__main__':
    create_dictionary("test_data/test_data1.csv")