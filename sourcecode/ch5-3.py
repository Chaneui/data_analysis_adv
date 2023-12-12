# button
def button_write():
    st.write('button activated')

st.button('Reset', type='primary')
st.button('activate', on_click=button_write) 

# 클릭 시 if문을 실행
st.button('Reset', type='primary')
if st.button('activate'):
    st.write('button activated')
    
