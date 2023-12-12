# title, header, subheader
import streamlit as st
import pandas as pd
from IPython import get_ipython

st.title('This is title')
st.header('This is header')
st.subheader('This is subheader')

# markdown
st.markdown(
    '''
    This is main text.
    This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)

# text
st.text(
    '''
    This is main text.
    This is how to change the color of text :red[Red,] :blue[Blue,] :green[Green.]
    This is **Bold** and *Italic* text
    '''
)

# code
code = '''
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
from matplotlib.dates import MonthLocator, DateFormatter

fig, ax = plt.subplots(figsize=(5,5))
sns.scatterplot(x='temp', y='count', data=df.head(40), s=100, ax=ax)
ax.yaxis.set_minor_locator(MultipleLocator(5))
ax.xaxis.set_minor_locator(MultipleLocator(1))
'''

st.code(code, language='python')

# divider
st.title('Title 1')
st.text('Text body 1')

st.divider()

st.title('Title 2')
st.text('Text body 2')