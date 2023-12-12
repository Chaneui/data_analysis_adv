df = pd.read_csv('datasets/Covid19-US/us_confirmed.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date').sort_values('Date')

# 특정 3개의 province/state 값을 선택하여 데이터 간소화
states = df['Province/State'].unique()[0:3]
df = df[df['Province/State'].isin(states)]

# 6개월의 기간 및 "Province/State" 열의 값으로 그룹화
df.groupby([pd.Grouper(freq='6m'), 'Province/State'])['Case'].mean()