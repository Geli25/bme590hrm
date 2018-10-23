import pandas as pd


def import_data(directory):
    headers = ['Time', 'Voltage']
    data = pd.read_csv(directory, names=headers)
    return data

