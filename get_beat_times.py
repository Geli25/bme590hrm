import numpy as np
import logging


def get_beat_times(peaks, data):
    """This function gets the time of which the peak occurred in the dataframe.

    The function accesses the "Time" column via the voltage signal of the peak.
    The numbers are rounded to 3 decimals (how it was recorded in the csv)
    to avoid numbers like .99999. Should be used after find_peak.py.

    Args:
        peaks(array): An array of information about the peak.
        data(dataframe): A pandas data frame with at least a "Time"
            and "Voltage" column.

    Returns:
        ndarray: A numpy array of times when a beat occurred.

    """
    try:
        beat_times = []
        beats_index = peaks[0][0]
        print(beats_index)
        for beat in beats_index:
            # print(beat)
            time_of_beat = data.loc[beat, "Time"]
            if time_of_beat.size == 0:
                raise ValueError
            mod_time_of_beat = round(time_of_beat, 3)
            # print(mod_time_of_beat)
            beat_times.append(mod_time_of_beat)
        numpy_beat_times = np.array(beat_times)
        print(numpy_beat_times[0], numpy_beat_times[-1])
        return numpy_beat_times
    except ValueError:
        logging.warning("No beat time detected, double check dataframe")
    except AttributeError:
        logging.error("The dataframe needs to have a Time header")
        return
    except IndexError:
        logging.error("Please find peak data via scipy.find_peaks()")
        return
