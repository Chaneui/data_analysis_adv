df = pd.read_csv('./datasets/bookings/bookings.csv')

# info 메서드를 이용한 데이터테이블의 개략적 정보 파악
df.info()

# describe 메서드를 이용한 데이터테이블의 수치형 통계정보 파악
df.describe()

# describe 메서드를 이용한 데이터테이블의 번주형 통계정보 파악
df.describe(include='object')

# 고유값과 고유값들이 나타나는 빈도수 구하기
df['Review'].value_counts()

# review 열의 일부 값 수정 및 value_counts 메서드 재실행
df.loc[df['Review'] == "Superb 9.0", "Review"] = "Superb "
df.loc[df['Review'] == "Exceptional 10", "Review"] = "Exceptional "

df['Review'].value_counts()

# unique 메서드를 이용한 고유값 확인
df['Total_Review'].unique()

# Total review 열 일부 값 수정 후 unique 메서드 재실행
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('external','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace('review','').strip())
df['Total_Review'] = df['Total_Review'].map(lambda x: str(x).replace(',',''))
df['Total_Review'] = df['Total_Review'].astype('float')

df['Total_Review'].describe()