from shape import rectangle,circle

def test_area(new_rectangle):
    assert new_rectangle.area() == 10 * 6


def test_perimeter(new_rectangle):
    assert new_rectangle.perimeter() == (10 + 6) * 2


def test_not_equal(new_rectangle, weird_rectangle):
    assert new_rectangle != weird_rectangle
    

