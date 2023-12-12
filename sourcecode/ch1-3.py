df = pd.read_csv('./datasets/bike_rentals/bike_rentals.csv')
df.info()

# select_dtypes 메서드를 사용하여 int형 변수만 선택
df.select_dtypes(include='int')

# select_dtypes 메서드를 사용하여 int형 변수만 제외하여 선택
df.select_dtypes(exclude='int')