import streamlit as st

def main():
    st.text_input("Enter your name:", key="name_input")
    st.number_input("Enter your age:", min_value=0, max_value=120, step=1, key="age_input")

if __name__ == "__main__":
    main()
