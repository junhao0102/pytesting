import pytest
#--單參數單次循環
# @pytest.mark.parametrize('name',['小明'])
# def test_para(name):
#     print(f'名字是{name}')
    
    
#--單參數多次循環
@pytest.mark.parametrize('name',['小明','小華','小美'])
def test_para(name):
    assert name == '小美'
    