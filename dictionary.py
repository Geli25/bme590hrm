from read_data import import_data
from validate_data import validate
from find_min_max import find_min_max
from find_peak import find_peak
from get_duration import get_duration
from get_beat_times import get_beat_times
from calculate_mean_bpm import calculate_mean_bpm


def create_dictionary(directory):
    """This function executes calculations of data & outputs "metrics" dictionary.

    Args:
        directory(string): Path to the file in a string format.

    Returns:
        dict: A dictionary with key value pairs of necessary ECG analysis data.

    """
    try:
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
    # Since the directory error is already handled by read_data
    # no need to do more logging
    except FileNotFoundError:
        return
    except ValueError:
        return
    except AttributeError:
        return
    except NameError:
        return

    print(metrics)
    return metrics
