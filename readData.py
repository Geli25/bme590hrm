import csv
import pandas as pd

def importdata(directory):
    headers=['Time','Voltage']
    data = pd.read_csv(directory , names=headers)
    return data



