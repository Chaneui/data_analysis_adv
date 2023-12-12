# booking 데이터셋을 불러와 total review 열의 값 수정
df = pd.read_csv('./datasets/bookings/bookings.csv')

df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')

# Total review 열의 값을 0부터 1까지의 0.2 단위 분위수 구하기
quantile = [0, 0.2, 0.4, 0.6, 0.8, 1]

for idx in quantile:
    q = df['Total_Review'].quantile(idx, interpolation='lower')
    print(f'quantile({idx}) is {q}')
    
# quantile 메서드의 interpolation 인자 수정
for idx in quantile:
    q = df['Total_Review'].quantile(idx, interpolation='nearest')
    print(f'quantile({idx}) is {q}')