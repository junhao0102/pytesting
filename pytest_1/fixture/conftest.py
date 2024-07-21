import pytest
from shape import rectangle


# ----fixture可以在多個測試案例中使用，可以將公共的部分提取出來，減少重複程式碼----
@pytest.fixture
def new_rectangle():
    return rectangle(10, 6)


@pytest.fixture
def weird_rectangle():
    return rectangle(2, 3)
