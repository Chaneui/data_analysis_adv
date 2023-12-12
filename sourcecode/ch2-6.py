df = pd.read_csv('datasets/Covid19-US/us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.info()

# head
df.head()

# datetime index를 가진 테이블의 시간 슬라이싱
df = df.set_index('Date').sort_values('Date')
df['2020-01':'2020-02']

# 문자열 index를 가진 데이터테이블
df = df.reset_index().set_index('Province/State').sort_index()
df.index.unique()

# 문자열의 일부만을 이용한 사전식 행 슬라이싱
df['Ca':'Df']