import numpy as np


def get_beat_times(peaks, data):
    beat_times = []
    beats_index = peaks[0][0]
    print(beats_index)
    for beat in beats_index:
        # print(beat)
        time_of_beat = data.loc[beat, "Time"]
        mod_time_of_beat = round(time_of_beat, 3)
        # print(mod_time_of_beat)
        beat_times.append(mod_time_of_beat)
    numpy_beat_times = np.array(beat_times)
    print(numpy_beat_times[0], numpy_beat_times[-1])
    return numpy_beat_times
