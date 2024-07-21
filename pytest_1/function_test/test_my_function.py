import pytest
from my_function import add, divide


def test_add():
    result = add(1, 2)
    assert result == 3

def test_add_string():
    result = add('hello', 'world')
    assert result == 'helloworld'
    
    


def test_dive():
    result = divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
