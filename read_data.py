import pandas as pd
import logging


def import_data(directory):
    """This function reads the csv files into a panda dataframe.

    The function loads all data from the csv file to a pandas dataframe,
    appendings two headers: Time and Voltage for easier access.

    Args:
        directory(string): File path to the csv file in string format.

    Returns:
        dataframe: A pandas dataframe array with all data in the csv file.

    """
    try:
        headers = ['Time', 'Voltage']
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
