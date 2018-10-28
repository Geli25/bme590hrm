import pandas as pd
import logging


def validate(input_data):
    """This function removes all "invalid" dataframe rows.

    The function goes through the data multiple times and removes
    all rows considered invalid. First it drops all rows containing
    NaN(automatically converted by pandas if the csv has an empty input),
    it then drops all rows containing strings (ex. 32c). One dataframe
    had problems with converting the format of the dataframe, so all dataframes
    are converted from objects to floats. Finally, all voltage values >300
    are removed.

    Args:
        input_data(dataframe):A pandas dataframe with all relevant data.

    Returns:
        dataframe: A filtered dataframe.

    """
    try:
        data = input_data.dropna()

        # Filter out all dataframe containing letters
        df = data[pd.to_numeric(data.Voltage, errors='coerce').notnull()]
        df2 = df[pd.to_numeric(df.Time, errors='coerce').notnull()]

        # Convert all dataframe into float
        df2.loc["Time"] = df2.Time.astype(float)
        df2.loc["Voltage"] = df2.Voltage.astype(float)
        df2["Voltage"] = df2.Voltage.astype(float)
        df2["Time"] = df2.Time.astype(float)
        print(df2.dtypes)

        # Filter out dataframe outside of range
        df3 = df2[df2['Voltage'] <= 300]
    except ValueError:
        logging.error("A panda dataframe is needed to run this method")
        return

    print(df3)
    return df3
