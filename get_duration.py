from readData import import_data
from validateData import validate


def get_duration(data):
    start_time = data.Time.min()
    end_time = data.Time.max()
    duration = end_time-start_time
    print(duration)
    return duration

if __name__ == '__main__':
    get_duration(validate(import_data("test_data/test_data32.csv")))