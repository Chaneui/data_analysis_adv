df = pd.read_csv('datasets/APPL_price/APPL_price.csv')
df.head()

# 시계열 컬럼의 인덱스 지정
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')
df.head()

# 시계열 데이터의 행 슬라이싱
df['1980-12-13':'1980-12-18']

# 시계열 데이터의 행 슬라이싱2
df['2015-02':'2015-02']