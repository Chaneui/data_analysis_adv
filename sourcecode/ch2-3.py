#
s = pd.Series([0, 0, 1, 1, 0, 1, 1, 1, 1, 0])
s

#
sc = s.cumsum()
sc

#
s.mul(sc)

#
s.mul(sc).diff()

#
s.mul(sc).diff().where(lambda x: x<0)

#
s.mul(sc).diff().where(lambda x: x<0).ffill()

#
s.mul(sc).diff().where(lambda x: x<0).ffill().add(sc, fill_value=0)

# 실전 데이터에 적용
df = pd.read_csv('datasets/APPL_price/APPL_price.csv')
s = df['Close'] > 175
s.sum()

# 실전 데이터에 적용
sc = s.cumsum()
s.mul(sc).diff().where(lambda x: x<0).ffill().add(sc, fill_value=0).max()