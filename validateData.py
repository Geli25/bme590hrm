import pandas as pd
import logging


def validate(input_data):
    # Filter out all NaN value
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

    print(df3)
    return df3
