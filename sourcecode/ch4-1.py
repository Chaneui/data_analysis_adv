import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')

fig, ax = plt.subplots()
sns.lineplot(x='Date', y='Close', data=df, ax=ax)

# info
df.info()

# Date 변수를 datetime 형으로 바꾼 후 그래프 재시각화
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots()
sns.lineplot(x='Date', y='Close', data=df, ax=ax)

# matplotlib의 major formatter 사용
import matplotlib as mpl

fig, ax = plt.subplots()
sns.lineplot(x='Date', y='Close', data=df, ax=ax)
ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

# Plotly로 시계열 그래프 시각화
import plotly.express as px

df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')

fig = px.line(df, x='Date', y='Close', width=500, height=400)
fig.show()

# Plotly로 그린 시계열 그래프의 x축 시간 포멧 변경
fig = px.line(df, x='Date', y='Close', width=500, height=400)
fig.update_xaxes(tickformat='%Y-%m-%d')
fig.show()
