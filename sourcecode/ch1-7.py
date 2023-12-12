df = pd.read_csv('./datasets/bookings/bookings.csv')
df.info()

# bookings 데이터셋에서 "Review" 열이 결측치인 행의 상위 5개 인덱스 호출
index = df[df['Rating'].isna()].head(5).index
index

# 해당 열의 평균값으로 결측치를 대체
df['Rating'] = df['Rating'].fillna(df['Rating'].mean())

# "Rating"열이 결측치였던 인덱스를 재호출
df.loc[index, 'Rating']

# 결측치를 포함하는 간단한 Pandas Series를 생성
import numpy as np
s = pd.Series([1, np.nan, np.nan,2, np.nan, 3])
s

# 결측치 이전에 있던 값으로 결측치를 대체
s.fillna(method='ffill')

# 결측치 이후에 나오는 값으로 이전 결측치를 대체
s.fillna(method='bfill')

# dropna 메서드를 이용한 결측치 제거
df = pd.read_csv('./datasets/bookings/bookings.csv')
df = df.dropna()
df.info()