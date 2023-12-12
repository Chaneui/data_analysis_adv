# selectbox
option = st.selectbox(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
)
st.text('you selected: {}'.format(option))

# selectbox placeholder 활용
option = st.selectbox(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
    index=None,
    placeholder='select transportation'
)
st.text('you selected: {}'.format(option))

# radio
option = st.radio(
    'What is your favorite movie genre',
    ["Comedy", "Drama", "Documentary"],
    captions = ['Laugh out loud', 'Get the popcorn', 'Never stop learning']
)

if option:
    st.text('You Selected {}'.format(option))
    
# multiselect
option = st.multiselect(
    label='your selection is',
    options=['Car', 'Airplane', 'Train', 'Ship'],
    placeholder='select transportation'
)
st.text('you selected: {}'.format(option))