def get_duration(data):
    """This function gets the duration of the ECG strip.

    Args:
        data(dataframe): A pandas dataframe with a column called "Time".

    Returns:
        float: The difference between the maximum and minimum recorded time.

    """
    start_time = data.Time.min()
    end_time = data.Time.max()
    duration = end_time-start_time
    print(duration)
    return duration
