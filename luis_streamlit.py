import streamlit as st
import pandas as pd

import numpy as np

st.write('drawing a dataframe')

df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40],
    'third column': [100,200,300,400]
})

df

st.write('showing a dataframe as a table')
dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

st.write('pandas dataframe styler')
dataframe = pd.DataFrame(np.random.randn(10,20),columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0))

st.write("static table")
dataframe = np.random.randn(10,20)
st.table(dataframe)


st.write('drawing a line chart')

chart_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(chart_data)


st.write('plotting a map')
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76,-122.4],
    columns=['lat','lon']
)

st.map(map_data)

st.write('widgets')
x = st.slider('x')
st.write(x, ' squared is ', x*x)

st.text_input('Your Name',key='name')
st.session_state.name


st.write('checkboxes')

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    chart_data


st.write('select box')
df = pd.DataFrame({
    'first column': [1,2,3,4],
    'second column': [10,20,30,40]
})

option = st.selectbox(
    'Which number do you like best?',
    df['first column']
)

'You selected: ', option

