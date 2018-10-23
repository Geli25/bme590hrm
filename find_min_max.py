import pandas as pd


def find_min_max(data):
    min = pd.data.Voltage.min()
    max = pd.data.Time.max()
    print(min,max)
    min_max = [min, max]
    return min_max