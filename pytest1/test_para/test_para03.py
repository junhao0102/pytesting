import requests

def test_request():
    url ='https://v6.exchangerate-api.com/v6/669dcc1331a174ba75adffd8/latest/USD' 
    res = requests.get(url)
    result = res.json()
    assert res.status_code == 200
    assert result['base_code'] == 'USD'
    assert result['result'] == 'success'