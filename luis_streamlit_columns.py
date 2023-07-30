import streamlit as st
import time

left_column, right_column = st.columns(2)

left_column.button('Press me!')

with right_column:
    chosen = st.radio(
        'Sorting hat',
        ('Gryffindor','Haffelpuff','Slytherin','Ravenclaw')
    )

    st.write(f'You are in {chosen} house!')

    'Starting a long computation...'

    latest_iteration = st.empty()

    bar = st.progress(0)

    for i in range(100):
        latest_iteration.text(f'Iteration {i+1}')
        bar.progress(i+1)
        time.sleep(0.1)

    '...and we are doneS'