# checkbox
active = st.checkbox('I agree')

if active:
    st.text('Great!')
    
# checkbox on_change 인자 활용
def checkbox_write():
    st.write('Great!')

st.checkbox('I agree', on_change=checkbox_write)

# toggle
toggle = st.toggle(
    'Turn on the switch!', value=True
)

if toggle:
    st.text('Switch is turned on!')
else:
    st.text('Switch is turned off!')

