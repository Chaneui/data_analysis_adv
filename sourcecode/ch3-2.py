df = sns.load_dataset('tips')
fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=df, ax=ax)

# 신뢰구간 삭제
fig, ax = plt.subplots()
sns.regplot(x='total_bill', y='tip', data=df, ax=ax, ci=None)

# 다항 함수 regression
import numpy as np

x = np.arange(0, 10, 1)
y = x**3 - 9*x**2 + x + 4

fig, ax = plt.subplots()
sns.regplot(x=x, y=y, ax=ax, order=3)

# 회귀선 모양 설정
fig, ax = plt.subplots()
sns.regplot(
    x=x, y=y, ax=ax, order=3,
    scatter_kws={'s':80}, line_kws={'color':'red', 'linestyle':'--'}
)

# Plotly로 회귀선 그리기
df = sns.load_dataset('tips')

fig = px.scatter(
    data_frame=df, x='total_bill', y='tip',
    width=400, height=400, trendline='ols'
)
fig.show()

# 특정 변수 그룹별 개별 회귀선 그리기
fig = px.scatter(
    data_frame=df, x='total_bill', y='tip',
    width=450, height=400,
    color='smoker', trendline='ols'
)
fig.show()