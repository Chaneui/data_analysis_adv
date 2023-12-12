# data query
def load_dataset(path):
    return pd.read_csv(path)

path = 'datasets/CO2_emissions/CO2_Emissions.csv'
df = load_dataset(path)
df.head().T

# sidebar 생성
makers = df['Vehicle Class'].unique().tolist()

with st.sidebar:
    st.markdown('Filter the data you want to analyze: :tulip:')
    
    st.multiselect(
        'Select the vehicle class you want to analyze: ',
        makers, default=['TWO-SEATER'],
        key='maker_filter'
    )
    
    st.slider(
        'Select the engine size (Liter) you want to analyze: ',
        min_value = df['Engine Size(L)'].min(),
        max_value = df['Engine Size(L)'].max(),
        value=(df['Engine Size(L)'].quantile(0.1), df['Engine Size(L)'].quantile(0.95)),
        step=.3,
        key='engine_filter'
    )
    
df = df.loc[
    (df['Vehicle Class'].isin(st.session_state['maker_filter'])) & 
    (df['Engine Size(L)'] < st.session_state['engine_filter'][1]) &
    (df['Engine Size(L)'] > st.session_state['engine_filter'][0])
    ]

# 메인 페이지 구성1
st.title(
    'Data Analysis - CO2 Emission'
)
st.write(
    '''
    Hello there, this web page is a simple data analysis web dashboard created using the Python Streamlit library.
    On this page, you can visualize the distribution of some variables or the correlation between variables.
    '''
)
st.divider()

# 메인 페이지 구성2 - 그래프 그리기
st.subheader(
    'Analysis of Engine Sizes'
)

col1, col2 = st.columns(2)
with col1:
    st.write(
        '''
        The box plot of engine sizes by automotive manufacturer. What types of engine sizes do manufacturers produce the most for each brand?
        '''
    )
with col2:
    fig1 = px.box(
        data_frame=df.sort_values('Engine Size(L)', ascending=False),
        x='Make', y='Engine Size(L)', width=300, height=400, points='all'
    )
    st.plotly_chart(fig1)

st.divider()

# 메인 페이지 구성3 - interactive 그래프 그리기
st.subheader(
    'Analysis of Fuel Consumption'
)

col3, col4 = st.columns(2)
with col3:
    st.write(
        '''
        The scatter plot graph illustrating fuel efficiency based on engine sizes.
        Which manufacturer might have lower fuel efficiency within the same engine size?
        Which manufacturer might have higher fuel efficiency within the same engine size?
        '''
    )
    st.selectbox(
        'Select Y-axis: ',
        [
            'Fuel Consumption City (L/100 km)',
            'Fuel Consumption Hwy (L/100 km)',
            'Fuel Consumption Comb (L/100 km)'
            ],
        key='fig2_yaxis'
    )
with col4:
    fig2 = px.scatter(
        data_frame=df, x='Engine Size(L)', y=st.session_state['fig2_yaxis'],
        width=500, color='Make', trendline='ols', trendline_scope='overall'
    )
    st.plotly_chart(fig2)

st.divider()

# 메인 페이지 구성4 - interactive 그래프 그리기
st.subheader(
    'Analysis of Carbon Emissions'
)

col5, col6 = st.columns(2)
with col5:
    st.write(
        '''
        The scatter plot graph depicting the correlation between fuel efficiency and carbon emissions, with color differentiation for each manufacturer.
        Which manufacturer might have higher carbon emissions within the same fuel efficiency range?
        '''
    )
    st.selectbox(
        'Select X-axis: ',
        [
            'Fuel Consumption City (L/100 km)',
            'Fuel Consumption Hwy (L/100 km)',
            'Fuel Consumption Comb (L/100 km)'
            ],
        key='fig3_xaxis'
    )
with col6:
    fig3 = px.scatter(
        data_frame=df, x=st.session_state['fig3_xaxis'], y='CO2 Emissions(g/km)',
        width=500, color='Make', trendline='ols', trendline_scope='overall'
    )
    st.plotly_chart(fig3)