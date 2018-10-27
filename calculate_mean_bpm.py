import numpy as np
import logging


def calculate_mean_bpm(data, beats, start_time=0, end_time=None):
    """This function calculates a bpm based on user indicated time frame.

    The function first selects the beat times within the indicated time frame
    and puts their index into a numpy array. It then takes the length of the array,
    which are the number of beats within that time frame, and divides it by the
    duration of the timeframe selected, giving the number of beats/second. Finally,
    it times that number by 60 and rounds it to a full number, getting the bpm.

    Args:
        data(dataframe): A pandas data frame with at least a "Time" and "Voltage" column.
        beats(ndarray): A numpy array of times when a peak occurred (from get_beat_times.py).
        start_time(int/float): The start of the desired time frame (seconds), default is 0.
        end_time(int/float): The end of the desired time frame (seconds),default is the time at the end of the strip.

    Returns:
        float: A number of the calculated value of beats at the given timeframe.

    """
    if end_time is None:
        end_time = data["Time"].iloc[-1]
    if end_time > data["Time"].iloc[-1]:
        logging.warning("End time is over the duration of the ECG strip.")
        end_time = data["Time"].iloc[-1]
    if start_time is None:
        start_time = 0
    beats_in_range = np.logical_and(beats >= start_time, beats <= end_time)
    beats_in_range_index = np.where(beats_in_range)
    print(start_time, end_time)
    print(beats_in_range_index[0].size)
    bpm = (beats_in_range_index[0].size/(end_time-start_time))*60
    # print(end_time-start_time)
    rounded_bpm = round(bpm, 0)
    print(rounded_bpm)
    return rounded_bpm
