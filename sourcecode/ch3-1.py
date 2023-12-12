import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

df = pd.read_csv('./datasets/global_internet_users/global_internet_users.csv')

# entity 변수 고유값 출력
df.Entity.unique()

# 임의 3 개의 entity 고유값을 가지는 행만 필터링
entities = ['China', 'India', 'Finland']
df = df.loc[df['Entity'].isin(entities)]

# Seaborn scatterplot을 entity 그룹별 색깔 구분하여 출력
fig, ax = plt.subplots()
sns.scatterplot(
    x='Year', y='No. of Internet Users', data=df, ax=ax, hue='Entity', palette='bright'
)

# seaborn scatterplot hue_order
fig, ax = plt.subplots()
sns.scatterplot(
    x='Year', y='No. of Internet Users', data=df, ax=ax,
    hue='Entity', hue_order=['India', 'Finland', 'China']
)

# seaborn scatterplot style
fig, ax = plt.subplots()
sns.scatterplot(
    x='Year', y='No. of Internet Users', data=df, ax=ax,
    style='Entity', markers=['o','^','X'], s=100
)

# seaborn scatterplot size
fig, ax = plt.subplots()
sns.scatterplot(
    x='Year', y='No. of Internet Users', data=df, ax=ax,
    size='Entity', sizes=(40, 200)
)

# tips 데이터셋을 이용한 Seaborn scatterplot
df = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='smoker', style='time', size='size'
)

# plotly scatterplot
import plotly.express as px
import pandas as pd

df = pd.read_csv('./datasets/global_internet_users/global_internet_users.csv')

fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400
)
fig.show()

# plotly scatterplot의 변수별 색깔 구분
entities = ['China', 'India', 'Finland']
df = df.loc[df['Entity'].isin(entities)]

fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, color='Entity'
)
fig.show()

# plotly scatterplot의 color_discrete_sequence 인자 활용
color = px.colors.qualitative.Light24
fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400,
    color='Entity', color_discrete_sequence=color
)
fig.show()

# plotly scatterplot의 변수별 scatter 모양 구분
fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, symbol='Entity'
)
fig.show()

# plotly scatterplot의 symbol_sequence 인자 활용
fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, symbol='Entity',
    symbol_sequence=['star','arrow','cross']
)
fig.show()

# plotly scatterplot의 변수별 scatter 크기 구분
fig = px.scatter(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, size='No. of Internet Users'
)
fig.show()

# plotly scatterplot의 color, size, symbol 인자 동시 사용
df = sns.load_dataset('tips')

fig = px.scatter(
    data_frame=df, x='total_bill', y='tip',
    color='smoker', size='size', symbol='time',
    width=600, height=400,
)
fig.show()