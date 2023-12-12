import pandas as pd
import numpy as np

df = pd.read_csv('datasets/Uber/Uber.csv')
df.head()

# info
df.info()

# unique
df['START_DATE*'] = pd.to_datetime(df['START_DATE*'], errors='coerce')
df['END_DATE*'] = pd.to_datetime(df['END_DATE*'], errors='coerce')
df = df.sort_values(['START_DATE*','END_DATE*'])

df['START_DATE*'].unique()

df['END_DATE*'].unique()

# value_counts
df['CATEGORY*'].value_counts()

df['START*'].value_counts()

df['STOP*'].value_counts()

# describe
df['MILES*'].describe()

# describe 메서드를 이용한 이상치 탐색
df[df['MILES*'] == df['MILES*'].max()]

# describe 메서드를 이용한 이상치 탐색 후 제거
df = df.drop(1155)
df['MILES*'].describe()

# value_counts2
df['PURPOSE*'].value_counts()

# isna와 sum 메서드를 이용한 결측치 개수 구하기
df['PURPOSE*'].isna().sum()

# datetime 변수의 단위 변환 (분)
df['DURATION*'] = (df['END_DATE*'] - df['START_DATE*']).dt.total_seconds() / 60
df['DURATION*']

# groupby를 이용한 그룹별 통계값 확인
df.groupby(['CATEGORY*','PURPOSE*'])[['MILES*','DURATION*']].agg(['mean','std','count'])

# 시각화를 통한 변수간 상관관계 확인
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import linregress

df = df.dropna()
s, i, r, _, _ = linregress(df['MILES*'], df['DURATION*'])

fig, ax = plt.subplots()
sns.regplot(x='MILES*', y='DURATION*', data=df, ax=ax,
            line_kws={'label':'y={:.2f}x+{:.2f}, R^2={:.2f}'.format(s, i, r**2)})
plt.legend()