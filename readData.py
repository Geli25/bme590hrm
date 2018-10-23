import pandas as pd


def import_data(directory):
    # adding headers to the dataframe
    headers = ['Time', 'Voltage']
    # reading data as panda dataframe
    data = pd.read_csv(directory, names=headers)
    return data
