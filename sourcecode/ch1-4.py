df = pd.read_csv('./datasets/bike_rentals/bike_rentals.csv')
df = df.set_index('datetime')

#'날짜 시:분:초' 형태로 이루어진 형태의 인덱스에서 00:00:00을 포함하는 인덱스만 선택
df.filter(like='00:00:00', axis=0)

# humidty와 windspeed 열만 필터링
df.filter(items=['humidity', 'windspeed'])

#열 이름 중에 'in'과 's' 사이에 임의의 한 문자를 지니는 열을 필터링
df.filter(regex='in.s')