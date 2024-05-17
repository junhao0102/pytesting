import streamlit as st

st.title("Bean counter :dog2:")
# Initialize st.session_state.beans
st.session_state.beans = st.session_state.get("beans", 0)


addend = st.number_input("Beans to add", 0, 10)


if st.button("Add"):
    st.session_state.beans += addend


st.markdown(f"Beans counted: {st.session_state.beans}")
