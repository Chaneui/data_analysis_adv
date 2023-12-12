df = pd.read_csv('datasets/product/product.csv')
df.head()

# join 메서드를 이용한 문자열 groupby
df['path'] = df.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
df['path']

# 각 "product_id" 값 당 하나의 행만 가지도록 데이터를 정리
df['path'] = df['factory'] + '_' + df['path']
df = df.drop_duplicates('product_id')
df = df[['date','product_id','passfail','path']]
df

# passfail 변수의 그룹화를 통해 path의 고유값과 빈도수 확인
df.groupby('passfail')['path'].value_counts()

# passfail 변수의 그룹화를 통해 date의 고유값과 빈도수 확인
df.groupby(['passfail'])['date'].value_counts()