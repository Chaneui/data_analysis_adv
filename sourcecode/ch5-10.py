# sidebar
st.title('This is main page')

with st.sidebar:
    st.title('This is sidebar')
    side_option = st.multiselect(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship','Bicycle'],
    placeholder='select transportation'
    )
    
# column 이해
img2 = Image.open('datasets/images/image2.jpg')
img3 = Image.open('datasets/images/image3.jpg')

st.header('Lemonade')
st.image(img2, width=300, caption='Image from Unsplash')

st.header('Cocktail')
st.image(img3, width=300, caption='Image from Unsplash')

# column 활용
col1, col2 = st.columns(2)

with col1:
    st.header('Lemonade')
    st.image(img2, width=300, caption='Image from Unsplash')

with col2:
    st.header('Cocktail')
    st.image(img3, width=300, caption='Image from Unsplash')
    
# tab
tab1, tab2 = st.tabs(['Table','Graph'])

df = pd.read_csv('datasets/medical_cost/medical_cost.csv')
df = df.query('region == "northwest"')

with tab1:
    st.table(df.head(5))

with tab2:
    fig = px.scatter(
        data_frame=df, x='bmi', y='charges'
    )
    st.plotly_chart(fig)
    
# expander
df = pd.read_csv('datasets/medical_cost/medical_cost.csv')
df = df.query('region == "northwest"')

fig = px.scatter(
        data_frame=df, x='bmi', y='charges'
    )
st.plotly_chart(fig)
    
with st.expander("See datatable"):
    st.table(df.head(5))