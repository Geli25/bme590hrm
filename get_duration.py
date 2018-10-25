def get_duration(data):
    start_time = data.Time.min()
    end_time = data.Time.max()
    duration = end_time-start_time
    print(duration)
    return duration
