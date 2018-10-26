import numpy as np
import logging


def calculate_mean_bpm(data, beats, start_time=0, end_time=None):
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