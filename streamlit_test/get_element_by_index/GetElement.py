import streamlit as st

def main():
    #容器1先於容器2建立,因此容器1的按鈕會在容器2的按鈕之前顯示,所以app_test.get("button")[0]會是Button 2
    container1 = st.container()
    container2 = st.container()
    
    with container2:
        st.button("Button 1")
    
    with container1:
        st.button("Button 2")

if __name__ == "__main__":
    main()
