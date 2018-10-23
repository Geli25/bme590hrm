from ..readData import import_data
from ..validateData import validate
import pytest


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
