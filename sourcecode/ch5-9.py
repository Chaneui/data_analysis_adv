# file uploader
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')

fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, hue='time')

# streamlit 대시보드에 표현
st.pyplot(fig)

# Plotly chart를 streamlit 대시보드에 표현
import plotly.express as px

fig2 = px.box(
    data_frame=df, x='day', y='tip',
    facet_col = 'smoker', facet_row = 'sex',
    width=800, height=800
)

st.plotly_chart(fig2)

# 위젯을 활용한 interactive 그래프 표현
x_options = ['day','size']
y_options = ['total_bill','tip']
hue_options = ['smoker','sex']

x_option = st.selectbox(
    'Select X-axis',
    index=None,
    options=x_options
)

y_option = st.selectbox(
    'Select Y-axis',
    index=None,
    options=y_options
)

hue_option = st.selectbox(
    'Select Hue',
    index=None,
    options=hue_options
)

if (x_option != None) & (y_option != None):
    if hue_option != None:
        fig3 = px.box(
            data_frame=df, x=x_option, y=y_option,
            color=hue_option, width=500
        )
    else:
        fig3 = px.box(
            data_frame=df, x=x_option, y=y_option,
            width=500
        )
    st.plotly_chart(fig3)
    
# 이미지 표현
from PIL import Image

img = Image.open('datasets/images/image1.jpg')
st.image(img, width=300, caption='Image from Unsplash')