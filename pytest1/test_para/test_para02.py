import pytest
#陣列格式
@pytest.mark.parametrize('name,age', [['Tom',18], ['Jerry', 30]])
def test_para02(name, age):
    assert isinstance(name, str)
    assert isinstance(age, int)
    
    
#元組格式
@pytest.mark.parametrize('name,age', [('Tom',18), ('Jerry', 30)])
def test_para02(name, age):
    assert isinstance(name, str) 
    assert isinstance(age, int)