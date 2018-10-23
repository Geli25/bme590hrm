from ..readData import import_data
import pytest


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
