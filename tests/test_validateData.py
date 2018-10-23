from readData import importdata
from validateData import validate
import pytest


@pytest.mark.parametrize("a, expected", [
    ("test_data/test_data1.csv", 10000),
    ("test_data/test_data2.csv", 10000),
    ("test_data/test_data30.csv", 9998),
    ("test_data/test_data31.csv", 9996),
    ("test_data/test_data32.csv", 10000)
])
def test_validate_data(a, expected):
    data = importdata(a)
    validated_data = validate(data)
    count_row = validated_data.shape[0]
    assert count_row == expected
