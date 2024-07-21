import pytest
import service
import requests
import unittest.mock as mock


# ----這個裝飾器用來模擬 service 模組中的 get_user_from_id 函數。你可以控制這個函數的行為，而不需要依賴它的實際實現----
@mock.patch("service.get_user_from_id")
def test_get_user_by_id(mock_get_user_from_id):
    mock_get_user_from_id.return_value = "Mocked Alice"
    user_name = service.get_user_from_id(2)
    assert user_name == "Mocked Alice"


@mock.patch("requests.get")
def test_get_users(mock_get):
    # 創建一個 Mock 對象
    mock_response = mock.Mock()
    mock_response.status_code = 200  # 設置狀態碼為 200
    mock_response.json.return_value = {"id": 1, "name": "Tom"}

    # 設置 mock 對象的返回值
    mock_get.return_value = mock_response

    # 調用 service 模組中的 get_users 函數
    data = service.get_users()

    # 驗證返回值
    assert data == {"id": 1, "name": "Tom"}


@mock.patch("requests.get")
def test_get_users_failed(mock_get):
    mock_response = mock.Mock()
    mock_response.status_code = 404
    mock_get.return_value = mock_response
    # 驗證是否拋出了 requests.HTTPError 異常
    with pytest.raises(requests.HTTPError):
        service.get_users()
