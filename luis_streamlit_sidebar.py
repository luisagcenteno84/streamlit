import streamlit as st

add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email','Home Phone','Mobile Phone')
)

add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0,100.0,(25.0,75.0)
)

add_selectbox
add_slider