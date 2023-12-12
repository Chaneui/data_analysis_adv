# 데이터 로드 후 나누어진 행 합치기 (ch2-9.py)
df = pd.read_csv('datasets/product/product.csv')
df['path'] = df.groupby('product_id')['operator'].transform(lambda x: '_'.join(x))
df['path'] = df['factory'] + '_' + df['path']
df = df.drop_duplicates('product_id')
df = df[['date','product_id','passfail','path']]

df['path'].head()

# path 열 기준으로 앞 2개 문자열, 이후 문자열을 분리
df['factory'] = df['path'].map(lambda x: x[0:2])
df['path'] = df['path'].map(lambda x: x[3:])

df.head()

# split 메서드를 이용해 "_" 기준 문자열 분리
df['path'] = df['path'].map(lambda x: x.split('_'))
df['path'].head()

# explode 메서드를 이용한 행 분리
df = df.explode('path')
df.head(9)

# 데이터셋의 공정별로 process 열 추가
process_map = {
    '1':'P1',
    '2':'P1',
    'V':'P2',
    'W':'P2',
    'X':'P3',
    'Y':'P3'
}

df['process'] = df['path'].map(process_map)
df = df.rename({'path':'operator'}, axis=1)

df.head(9)