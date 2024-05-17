from streamlit.testing.v1 import AppTest

def test_app():
    at = AppTest.from_file("app_key.py")
    
    # 運行應用程序
    at.run()
    
     # 檢索帶鍵的部件
    name_input = at.text_input("name_input")
    age_input = at.number_input("age_input")
    
    # 檢查部件是否正確檢索
    assert name_input.label == "Enter your name:"
    assert age_input.label == "Enter your age:"
