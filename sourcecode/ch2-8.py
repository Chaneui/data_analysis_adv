df = pd.read_csv('datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])
df.head()

# 특정 변수의 그룹별 평균치 계산
df.groupby('inspection_step')['value'].mean()

# data normalization 1
df['normalized1'] = df.groupby('inspection_step')['value'].transform(lambda x: (x - x.mean())/x.std())
df['normalized1']

# inspection_step 변수의 고유값 별 가장 빠른 date를 가지는 행만 추출
temp = df.sort_values(['inspection_step','date']).drop_duplicates('inspection_step')
temp

# "temp"에 저장된 서브 데이터셋에서 "inspection_step" 열을 인덱스로 설정
# 인덱스와 value 열만 남김
temp = temp.set_index('inspection_step')['value']
temp

# data normalization 2
df = df.set_index('inspection_step')
df['normalized2'] = df['value'] - temp
df = df.reset_index()