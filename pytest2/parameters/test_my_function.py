import pytest
from my_function import add, divide
import time


def test_add():
    result = add(1, 2)
    assert result == 3


def test_add_string():
    result = add("hello", "world")
    assert result == "helloworld"


def test_dive():
    result = divide(4, 2)
    assert result == 2


def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
        
#----這樣的標記可以用來警告測試運行可能會比較慢，或者在執行測試時選擇性地運行或排除它們。----
@pytest.mark.slow
def very_slow():
    time.sleep(10)
    result = divide(4, 2)
    assert result == 2


#----skip標記可以用來跳過測試，而不是運行它們。----
@pytest.mark.skip(reason="This feature is broken")
def test_add2():
    result = add(1, 2)
    assert result == 3
    
#----xfail標記可以用來標記測試，即使它們失敗，也不會導致測試運行失敗。----
@pytest.mark.xfail(reason="We cannot divide by zero")
def test_divide_by_zero_broken():
    divide(1, 0)