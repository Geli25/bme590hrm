import logging


def find_min_max(data):
    """This functions finds the minimum and maximum voltage in all dataframe.

    Args:
        data(dataframe):A pandas dataframe with a column named "Voltage".

    Returns:
        tuple: A tuple containing the minimum and maximum values of the data.
        Minimum is the first returned value, and maximum, the second.

    """
    try:
        ecg_min = data.Voltage.min()
        ecg_max = data.Voltage.max()
        min_max = (ecg_min, ecg_max)
        print(min_max)
        return min_max
    except AttributeError:
        logging.error("Data needs to have at least a Voltage header.")
        return
