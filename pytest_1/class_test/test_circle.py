import pytest

from shape import circle


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        assert self.circle.area() == 3.14 * self.circle.radius**2

    def test_perimeter(self):
        result = self.circle.perimeter()
        expected = 2 * 3.14 * self.circle.radius
        assert result == expected
        