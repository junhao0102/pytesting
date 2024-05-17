import requests
import pytest

url1="https://www.twse.com.tw/exchangeReport/STOCK_DAY?response=json&date=20220421&stockNo=2330&_=1648189327587"
url2 ='https://v6.exchangerate-api.com/v6/669dcc1331a174ba75adffd8/latest/USD' 

@pytest.fixture(autouse=True)
def fun():
    print('我是前置步驟~~~~')
    
    
def test_request1():
    res = requests.get(url1)
    assert res.status_code == 200
 
def test_request2():
    res = requests.get(url2)
    result = res.json()
    assert res.status_code == 201
    assert result['base_code'] == 'USD'
    assert result['result'] == 'success'
    # assert result['conversion_rates']['USD'] == 1
    # assert result['conversion_rates']['AED'] == 3.67
    # assert result['conversion_rates']['AFN'] == 77.15
    # assert result['conversion_rates']['ALL'] == 102.09
    # assert result['conversion_rates']['AMD'] == 484.45
    
    
    
if __name__ == '__main__':
    pytest.main()