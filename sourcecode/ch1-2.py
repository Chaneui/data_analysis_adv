df = pd.read_csv('./datasets/bike_rentals/bike_rentals.csv')

# iloc을 이용한 행 선택
df.iloc[2:5, 3:6]

# loc을 이용한 행 선택
df.loc[2:4, 'workingday':'temp']

# season 열의 값이 2인 행들만 선택
df.loc[df['season'] == 2]

# season이 2인 행들 중에 casual, resistered, count 열만 선택
df.loc[df['season'] == 2, 'casual':]

#season이 1이 아니면서 동시에 weather가 2가 아닌 모든 행 선택
df.loc[(df['season'] != 1) & (df['weather'] != 2)]

#season이 1이 아니면서 동시에 weather가 2가 아닌 모든 행 선택, ~ 사용
df.loc[~(df['season'] == 1) & ~(df['weather'] == 2)]