import pandas as pd
import logging


def import_data(directory):
    try:
        # adding headers to the dataframe
        headers = ['Time', 'Voltage']
        # reading data as panda dataframe
        data = pd.read_csv(directory, names=headers)
    except FileNotFoundError:
        logging.error("The file either does not exist/file path is wrong")
        return
    except ValueError:
        logging.error("A path is needed to run this function")
        return
    except NameError:
        logging.error("The file path needs to be a string")
        return
    return data
