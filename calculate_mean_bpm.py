import numpy as np
import logging

from read_data import import_data
from validate_data import validate
from find_peak import find_peak
from get_beat_times import get_beat_times


def calculate_mean_bpm(data, beats, start_time=None, end_time=None):
    """This function calculates a bpm based on user indicated time frame.

    The function first selects the beat times within the indicated time frame
    and puts their index into a numpy array. It then takes the length of the
    array, which are the number of beats within that time frame, and divides
    it by the duration of the timeframe selected, giving the number of
    beats/second. Finally, it times that number by 60 and rounds it to a
    full number, getting the bpm.

    Args:
        data(dataframe): A pandas data frame with at least a "Time"
            and "Voltage" column.
        beats(ndarray): A numpy array of times when a peak occurred
            (from get_beat_times.py).
        start_time(int/float): The start of the desired time frame (seconds),
            default is 0.
        end_time(int/float): The end of the desired time frame (seconds),
            default is the time at the end of the strip.

    Returns:
        float: A number of the calculated value of beats at the given
        timeframe.

    """
    try:
        if type(beats) is not np.ndarray:
            logging.error("Second argument needs to be a numpy array")
            raise TypeError
        if end_time is None:
            end_time = data["Time"].iloc[-1]
        if end_time > data["Time"].iloc[-1]:
            raise ValueError
        if end_time < 0:
            raise ValueError
        if start_time is None:
            start_time = data["Time"].iloc[0]
        if start_time < 0:
            raise ValueError
        if start_time > end_time:
            raise ValueError
        in_rg = np.logical_and(beats >= start_time, beats <= end_time)
        beats_in_range_i = np.where(in_rg)
        print(start_time, end_time)
        print(beats_in_range_i[0].size)
        bps = beats_in_range_i[0].size / (end_time - start_time)
        bpm = bps * 60
        # print(end_time-start_time)
        rounded_bpm = round(bpm, 0)
        print(rounded_bpm)
        return rounded_bpm
    except ValueError:
        if type(beats) is not np.ndarray:
            logging.error("Second argument needs to be a numpy array")
            return
        try:
            if start_time < 0:
                logging.warning("Input invalid, switched to default")
                if end_time > data["Time"].iloc[-1] or end_time < 0:
                    end_time = data["Time"].iloc[-1]
                    start_time = data["Time"].iloc[0]
                    in_rg = np.logical_and(beats >= start_time, beats <= end_time)
                    beats_in_range_i = np.where(in_rg)
                    print(start_time, end_time)
                    print(beats_in_range_i[0].size)
                    bps = beats_in_range_i[0].size / (end_time - start_time)
                    bpm = bps * 60
                    # print(end_time-start_time)
                    rounded_bpm = round(bpm, 0)
                    print(rounded_bpm)
                    return rounded_bpm
            if end_time > data["Time"].iloc[-1] or end_time < 0:
                if start_time > end_time:
                    start_time = data["Time"].iloc[0]
                logging.warning("Input invalid, using default")
                end_time = data["Time"].iloc[-1]
                in_rg = np.logical_and(beats >= start_time, beats <= end_time)
                beats_in_range_i = np.where(in_rg)
                print(start_time, end_time)
                print(beats_in_range_i[0].size)
                bps = beats_in_range_i[0].size / (end_time - start_time)
                bpm = bps * 60
                # print(end_time-start_time)
                rounded_bpm = round(bpm, 0)
                print(rounded_bpm)
                return rounded_bpm
            if start_time < 0 or start_time > end_time:
                if start_time > end_time:
                    end_time = data["Time"].iloc[-1]
                logging.warning("Input invalid, using default")
                start_time = data["Time"].iloc[0]
                in_rg = np.logical_and(beats >= start_time, beats <= end_time)
                beats_in_range_i = np.where(in_rg)
                print(start_time, end_time)
                print(beats_in_range_i[0].size)
                bps = beats_in_range_i[0].size / (end_time - start_time)
                bpm = bps * 60
                # print(end_time-start_time)
                rounded_bpm = round(bpm, 0)
                print(rounded_bpm)
                return rounded_bpm
        except TypeError:
            if type(start_time) is str:
                logging.warning("Input must be a float or int, using default")
                start_time = data["Time"].iloc[0]
                end_time = data["Time"].iloc[-1]
                in_rg = np.logical_and(beats >= start_time, beats <= end_time)
                beats_in_range_i = np.where(in_rg)
                print(start_time, end_time)
                print(beats_in_range_i[0].size)
                bps = beats_in_range_i[0].size / (end_time - start_time)
                bpm = bps * 60
                # print(end_time-start_time)
                rounded_bpm = round(bpm, 0)
                print(rounded_bpm)
                return rounded_bpm
    except TypeError:
        if type(end_time) is str and type(start_time) is str:
            logging.warning("Input must be a float or int, using default")
            end_time = data["Time"].iloc[-1]
            start_time = data["Time"].iloc[0]
            in_rg = np.logical_and(beats >= start_time, beats <= end_time)
            beats_in_range_i = np.where(in_rg)
            print(start_time, end_time)
            print(beats_in_range_i[0].size)
            bps = beats_in_range_i[0].size / (end_time - start_time)
            bpm = bps * 60
            # print(end_time-start_time)
            rounded_bpm = round(bpm, 0)
            print(rounded_bpm)
            return rounded_bpm
        if type(end_time) is str:
            logging.warning("Input must be a float or int, using default")
            start_time = data["Time"].iloc[0]
            end_time = data["Time"].iloc[-1]
            in_rg = np.logical_and(beats >= start_time, beats <= end_time)
            beats_in_range_i = np.where(in_rg)
            print(start_time, end_time)
            print(beats_in_range_i[0].size)
            bps = beats_in_range_i[0].size / (end_time - start_time)
            bpm = bps * 60
            # print(end_time-start_time)
            rounded_bpm = round(bpm, 0)
            print(rounded_bpm)
            return rounded_bpm
        if type(start_time) is str:
            logging.warning("Input must be a float or int, using default")
            start_time = data["Time"].iloc[0]
            in_rg = np.logical_and(beats >= start_time, beats <= end_time)
            beats_in_range_i = np.where(in_rg)
            print(start_time, end_time)
            print(beats_in_range_i[0].size)
            bps = beats_in_range_i[0].size / (end_time - start_time)
            bpm = bps * 60
            # print(end_time-start_time)
            rounded_bpm = round(bpm, 0)
            print(rounded_bpm)
            return rounded_bpm
    except IndexError:
        logging.error("First parameter must be a pandas dataframe")
        return

#
# if __name__ == '__main__':
#     data=validate(import_data("test_data/test_data15.csv"))
#     peaks=find_peak(data)
#     beats=get_beat_times(peaks,data)
#     calculate_mean_bpm(data,beats,"hey",20)
