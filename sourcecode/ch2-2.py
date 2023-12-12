df = pd.read_csv('datasets/German_credit/German_credit.csv')
df.head()

# describe를 통한 Age 변수 확인
df['Age'].describe()

# cut 메서드를 이용한 수치형 변수 구간화
pd.cut(df['Age'], bins=8)

# 구간별 데이터 개수 확인
pd.cut(df['Age'], bins=8).reset_index().groupby('Age').size()

# cut 메서드를 통한 임의 구간화
bins = [10, 20, 30, 40, 50, 60, 70, 80]
pd.cut(df['Age'], bins=bins)

# right 인자를 이용한 오른쪽 닫힌 구간 범주화
bins = [10, 20, 30, 40, 50, 60, 70, 80]
pd.cut(df['Age'], bins=bins, right=False)

# qcut
pd.qcut(df['Age'], q=8)

# qcut으로 나눈 범주형 변수의 구간별 데이터 개수 확인
pd.qcut(
    df['Age'], q=8, duplicates='drop'
).reset_index().groupby('Age').size()