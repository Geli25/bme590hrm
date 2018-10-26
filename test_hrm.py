import pytest
from readData import import_data
from validateData import validate
from find_min_max import find_min_max
from find_peak import find_peak
from get_duration import get_duration
from get_beat_times import get_beat_times
from calculate_mean_bpm import calculate_mean_bpm
from dictionary import create_dictionary
from dictionary_output import output_json


@pytest.mark.parametrize("directory, expected", [
    ("test_data/test_data1.csv", 10000),
    ("test_data/test_data2.csv", 10000),
    ("test_data/test_data31.csv", 10000),
    ("test_data/test_data32.csv", 10000)
])
def test_import_data(directory, expected):
    data = import_data(directory)
    # calculating the number of rows after loading to see if all are loaded
    count_row = data.shape[0]
    assert count_row == expected


@pytest.mark.parametrize("directory, expected", [
    ("test_data/test_data1.csv", 10000),
    ("test_data/test_data2.csv", 10000),
    ("test_data/test_data30.csv", 9998),
    ("test_data/test_data31.csv", 9996),
    ("test_data/test_data32.csv", 9601)
])
def test_validate_data(directory, expected):
    data = import_data(directory)
    validated_data = validate(data)
    # calculating the number of rows after filtering to see if it is correct
    count_row = validated_data.shape[0]
    assert count_row == expected


@pytest.mark.parametrize("directory, expected", [
    ("test_data/test_data24.csv", (-1.73, 5.1175)),
    ("test_data/test_data27.csv", (-2.2825, 1.5025)),
    ("test_data/test_data30.csv", (-1.73, 5.1175)),
    ("test_data/test_data31.csv", (-0.19375, 0.7875)),
    ("test_data/test_data32.csv", (-375.0, 300.0))
])
def test_find_min_max(directory, expected):
    data = import_data(directory)
    validated_data = validate(data)
    min_max = find_min_max(validated_data)
    assert min_max == expected


@pytest.mark.parametrize("directory,expected", [
    ("test_data/test_data17.csv", 19),
    ("test_data/test_data1.csv", 35),
    ("test_data/test_data30.csv", 37),
    ("test_data/test_data31.csv", 19),
    ("test_data/test_data32.csv", 19)
])
def test_find_peak(directory, expected):
    data = import_data(directory)
    validated_data = validate(data)
    peaks = find_peak(validated_data)
    assert peaks[1] == expected


@pytest.mark.parametrize("directory,expected", [
    ("test_data/test_data15.csv", 13.887),
    ("test_data/test_data1.csv", 27.775),
    ("test_data/test_data30.csv", 39.996),
    ("test_data/test_data31.csv", 13.887),
    ("test_data/test_data32.csv", 13.887)
])
def test_get_duration(directory, expected):
    data = import_data(directory)
    validated_data = validate(data)
    duration = get_duration(validated_data)
    assert duration == expected


@pytest.mark.parametrize("directory,expected", [
    ("test_data/test_data1.csv", [0.214, 27.772]),
    ("test_data/test_data20.csv", [0.043, 13.543]),
    ("test_data/test_data30.csv", [0.16, 39.436]),
    ("test_data/test_data31.csv", [0.042, 13.537]),
    ("test_data/test_data32.csv", [0.028, 13.003])
])
def test_get_duration(directory, expected):
    data = import_data(directory)
    validated_data = validate(data)
    peaks = find_peak(validated_data)
    beat_times = get_beat_times(peaks, validated_data)
    time_check = [beat_times[0], beat_times[-1]]
    assert time_check == expected


@pytest.mark.parametrize("directory, start_time, end_time, expected", [
    ("test_data/test_data15.csv", 1, 30, 154),
    ("test_data/test_data25.csv", 2, 5, 60),
    ("test_data/test_data30.csv", 0, 10, 54),
    ("test_data/test_data31.csv", None, None, 82),
    ("test_data/test_data32.csv", 10, 20, 77)
])
def test_calculate_mean_bpm(directory, start_time, end_time, expected):
    data = validate(import_data(directory))
    peaks = find_peak(data)
    beats = get_beat_times(peaks, data)
    mean_bpm = calculate_mean_bpm(data, beats, start_time, end_time)
    assert mean_bpm == expected


@pytest.mark.parametrize("directory, expected", [
    ("test_data/test_data5.csv", [76, (-1.155, 1.72)]),
    ("test_data/test_data17.csv", [82, (-0.275, 0.7)]),
    ("test_data/test_data30.csv", [56, (-1.73, 5.1175)]),
    ("test_data/test_data31.csv", [82, (-0.19375, 0.7875)]),
    ("test_data/test_data32.csv", [82, (-375.0, 300.0)])
])
def test_calculate_mean_bpm(directory, expected):
    dictionary = create_dictionary(directory)
    results = [dictionary["mean_hr_bpm"], dictionary["voltage_extremes"]]
    assert results == expected

