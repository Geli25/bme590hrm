from ..readData import import_data
from ..validateData import validate
from ..find_min_max import find_min_max
import pytest


@pytest.mark.parametrize("a, expected", [
    ("test_data/test_data24.csv", (1.73, 5.1175)),
    ("test_data/test_data27.csv", (-2.2825, 1.5025)),
    ("test_data/test_data30.csv", (1.73, 5.1175)),
    ("test_data/test_data31.csv", (-0.19375, 0.7875)),
    ("test_data/test_data32.csv", (-375.0, 300.0))
])
def test_find_min_max(a, expected):
    data = import_data(a)
    validated_data = validate(data)
    min_max = find_min_max(validated_data)
    assert min_max == expected
