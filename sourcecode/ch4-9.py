df = sns.load_dataset('mpg')

fig, ax = plt.subplots()
sns.regplot(x='horsepower', y='weight', data=df, ax=ax)

# 선형 회귀식 구하기
from scipy.stats import linregress

s, i, r, p, se = linregress(df['horsepower'], df['weight'])
print('y={:.2f}x+{:.2f}, R^2={:.2f}'.format(s, i, r**2))

# info 메서드
df.info()

# dropna 수행 후 선형회귀식 시각화
df = df.dropna()
s, i, r, p, se = linregress(df['horsepower'], df['weight'])

fig, ax = plt.subplots()
sns.regplot(
    x='horsepower', y='weight', data=df, ax=ax,
    line_kws={'label':'y={:.2f}x+{:.2f}, R^2={:.2f}'.format(s, i, r**2)}
)
ax.legend()

# text 메서드를 이용한 선형회귀식 시각화
fig, ax = plt.subplots()
sns.regplot(x='horsepower', y='weight', data=df, ax=ax)
ax.text(
    x=0.05, y=0.9,
    s='y={:.2f}x+{:.2f}, R^2={:.2f}'.format(s, i, r**2),
    transform=ax.transAxes
)
# Plotly trendline을 이용한 회귀식 표현
fig = px.scatter(
    df, x='horsepower', y='weight', width=500, height=400,
    trendline='ols'
)

results = px.get_trendline_results(fig)
results = results.iloc[0]["px_fit_results"]
print(results.summary())

# Plotly trendline을 이용한 회귀식 파라메터 확인
results.params

# Plotly add_annotation 메서드를 이용한 선형회귀식 시각화
fig = px.scatter(
    df, x='horsepower', y='weight', width=500, height=400,
    trendline='ols'
)

fig.add_annotation(
    text='y= {:.1f}x + {:.1f}, R^2={:.2f}'.format(results.params[0], results.params[0], results.rsquared),
    x=0.05, y=0.95, xref='x domain', yref='y domain', showarrow=False
)

fig.show()