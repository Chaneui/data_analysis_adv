df = pd.read_csv('./datasets/bike_rentals/bike_rentals.csv')

# 열 이름 변경
df.rename(
    {'registered':'registered_user',
    'casual':'unregistered_user'},
    axis=1
)

# column 인자 사용하기
df.rename(
    columns={'registered':'registered_user',
           'casual':'unregistered_user'}
)