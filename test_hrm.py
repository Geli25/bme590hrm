import pytest
from readData import import_data
from validateData import validate
from find_min_max import find_min_max


@pytest.mark.parametrize("a, expected", [
    ("test_data/test_data1.csv", 10000),
    ("test_data/test_data2.csv", 10000),
    ("test_data/test_data31.csv", 10000),
    ("test_data/test_data32.csv", 10000)
])
def test_import_data(a, expected):
    data = import_data(a)
    # calculating the number of rows after loading to see if all are loaded
    count_row = data.shape[0]
    assert count_row == expected


@pytest.mark.parametrize("a, expected", [
    ("test_data/test_data1.csv", 10000),
    ("test_data/test_data2.csv", 10000),
    ("test_data/test_data30.csv", 9998),
    ("test_data/test_data31.csv", 9996),
    ("test_data/test_data32.csv", 9601)
])
def test_validate_data(a, expected):
    data = import_data(a)
    validated_data = validate(data)
    # calculating the number of rows after filtering to see if it is correct
    count_row = validated_data.shape[0]
    assert count_row == expected


@pytest.mark.parametrize("a, expected", [
    ("test_data/test_data24.csv", (-1.73, 5.1175)),
    ("test_data/test_data27.csv", (-2.2825, 1.5025)),
    ("test_data/test_data30.csv", (-1.73, 5.1175)),
    ("test_data/test_data31.csv", (-0.19375, 0.7875)),
    ("test_data/test_data32.csv", (-375.0, 300.0))
])
def test_find_min_max(a, expected):
    data = import_data(a)
    validated_data = validate(data)
    min_max = find_min_max(validated_data)
    assert min_max == expected
