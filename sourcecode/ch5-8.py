# file uploader
file = st.file_uploader(
    'Choose a file', type='csv', accept_multiple_files=False
)
if file is not None:
    df = pd.read_csv(file)
    st.write(df)