# text input
string = st.text_input(
    'Movie title', placeholder='write down the title of your favorite movie'
)

if string:
    st.text('Your answer is '+string)
    
# password 인자 활용
string = st.text_input(
    'Movie title',
    placeholder='write down the title of your favorite movie',
    type='password'
)

if string:
    st.text('Your answer is '+string)