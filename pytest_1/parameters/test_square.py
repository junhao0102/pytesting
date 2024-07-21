import pytest
from shape import square


@pytest.mark.parametrize(
    "side_length, expected_area", [(1, 1), (2, 4), (3, 9), (4, 16)]
)
def test_multiple_square_areas(side_length, expected_area):
    assert square(side_length).area() == expected_area


@pytest.mark.parametrize("side_length,expected_perimeter", [(3, 12), (4, 16), (5, 20)])
def test_multiple_square_perimeter(side_length, expected_perimeter):
    assert square(side_length).perimeter()== expected_perimeter
