import seaborn as sns

df = sns.load_dataset('titanic')
df.head()

# titanic 데이터셋의 성별에 대한 생존율을 비교
df.groupby('sex')['survived'].mean()

# titanic 데이터셋의 성별과 좌석 등급에 대한 생존율을 비교
df.groupby(['sex','class'])['survived'].mean()

# agg를 이용한 다양한 집계 함수 사용
df.groupby(['sex','class'])['survived'].agg(['mean','count'])

# agg와 딕셔너리를 이용한 컬럼별 다른 집계 함수 사용
df.groupby(['sex','class'])[['survived','age']].agg({'survived':'mean', 'age':'max'})

# apply 메서드를 이용한 사용자 정의 함수 사용
def get_IQR(data):
    _3rd = data.quantile(.75)
    _1st = data.quantile(.25)
    return (np.abs(_3rd - _1st) * 1.5)

df.groupby(['sex','class'])['age'].apply(get_IQR)

# penguins를 이용한 추가 데이터셋 로드
df = sns.load_dataset('penguins')
df.isna().sum()

# penguins 데이터셋의 종 별 평균값 비교
df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].mean()

# lambda 함수를 이용한 그룹별 평균치로 결측치 대체
df.groupby('species')[['bill_length_mm','bill_depth_mm','flipper_length_mm','body_mass_g']].apply(lambda x: x.fillna(x.mean()))

# groupby의 인자로 사용할 수 있는 다양한 데이터 형식들
df = pd.DataFrame(
    {'group':['A','A','A','B','B'],
    'value':[1, 1, 1, 10, 10]}
)
df

# groupby의 인자로 사용할 수 있는 다양한 데이터 형식들: 리스트
df.groupby([0,0,1,1,1])['value'].sum()

# groupby의 인자로 사용할 수 있는 다양한 데이터 형식들: Pandas Seires
s = pd.Series([False, False, True, True, True])
df.groupby(s)['value'].sum()