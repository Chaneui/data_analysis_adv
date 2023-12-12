df = pd.read_csv('datasets/weight_height/weight_height.csv')
df.describe()

# 이상치 확인을 위한 데이터 시각화
import seaborn as sns
sns.scatterplot(x='Weight', y='Height', data=df)

# query 메서드를 이용한 이상치 제거
df_new = df.query('Weight < 350')
df_new.describe()

# quantile 메서드를 이용한 이상치 기준 설정
criteria = df['Weight'].quantile(0.9999)
criteria

# 이상치 제거 후 시각화
df_new = df[df['Weight'] < criteria]
sns.scatterplot(x='Weight', y='Height', data=df_new)

# 특정 값 이상의 데이터 인덱스 확인
df[df['Weight'] > 390].index

# clip 메서드를 이용한 이상치 제거
df['Weight'] = df['Weight'].clip(50, 300)
df.iloc[2014]