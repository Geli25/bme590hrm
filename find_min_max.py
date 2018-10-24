from readData import import_data
from validateData import validate


def find_min_max(data):
    ecg_min = data.Voltage.min()
    ecg_max = data.Voltage.max()
    min_max = (ecg_min, ecg_max)
    print(min_max)
    return min_max

