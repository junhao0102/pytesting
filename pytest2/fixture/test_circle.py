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
    
    
    #----fixture可以在不同的檔案中使用,預設在conftest.py中----
    def test_not_as_area(self,new_rectangle):
        assert self.circle.area() != new_rectangle.area()
