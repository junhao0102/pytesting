from streamlit.testing.v1 import AppTest

def test_app():
    at = AppTest.from_file("GetElement.py")

    # 運行應用程序
    at.run()
    
    # 檢索按鈕元素
    button1 = at.button[0]
    button2 = at.button[1]
    
    # 檢查按鈕文本
    assert button1.label == "Button 2"
    assert button2.label == "Button 1"
