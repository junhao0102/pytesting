from streamlit.testing.v1 import AppTest

def test_increment_and_add():
    at = AppTest.from_file("add.py").run() #初始化模擬應用程式並執行第一個腳本運行
    at.number_input[0].increment().run() 
    at.number_input[0].increment().run()   #模擬使用者點擊加號圖示（新增）以增加輸入的數字（以及重新執行產生的腳本）
    at.button[0].click().run() 
    at.button[0].click().run()                   #模擬使用者點擊按鈕以執行產生的腳本
    assert at.markdown[0].value == "Beans counted: 4"   #確保標記已更新以顯示新的計數值