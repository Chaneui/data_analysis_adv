# matplotlib subplots를 이용한 2x2 subplot 생성
fig, ax = plt.subplots(2, 2, figsize=(12, 12))

# matplotlib 2x2 subplot에 Seaborn regplot 시각화
df = pd.read_csv('./datasets/medical_cost/medical_cost.csv')

fig, ax = plt.subplots(2, 2, figsize=(12, 12))
sns.regplot(
    x='bmi', y='charges', data=df.query('region == "southwest"'),
    ax=ax[0][0]
)
ax[0][0].set_title('region : southwest')

sns.regplot(
    x='bmi', y='charges', data=df.query('region == "southeast"'),
    ax=ax[0][1]
)
ax[0][1].set_title('region : southeast')

sns.regplot(
    x='bmi', y='charges', data=df.query('region == "northwest"'),
    ax=ax[1][0]
    )
ax[1][0].set_title('region : northwest')

sns.regplot(
    x='bmi', y='charges', data=df.query('region == "northeast"'),
    ax=ax[1][1]
    )
ax[1][1].set_title('region : northeast')

# seaborn lmplot으로 동일한 plot 그리기
sns.lmplot(
    x='bmi', y='charges', data=df,
    col='region', col_wrap=2,
    sharex=False, sharey=False
)

# seaborn lmplot의 hue 인자 활용
sns.lmplot(
    x='bmi', y='charges', data=df,
    col='smoker', row='region', hue='sex',
    sharex=False, sharey=False
)

# Seaborn facetgrid를 활용한 boxplot 나누어 그리기
g = sns.FacetGrid(
    data=df, col='region', col_wrap=2, sharex=False, sharey=False
)
g.map_dataframe(
    sns.boxplot, x='smoker', y='charges', hue='sex'
)

# Plotly facet을 활용한 scatterplot을 subplot에 나누어 그리기
fig = px.scatter(
    data_frame=df, x='bmi', y='charges',
    color='sex', facet_row='region', facet_col='smoker',
    width=700, height=1200, trendline='ols'
)
fig.show()

# Plotly facet을 활용한 boxplot을 subplot에 나누어 그리기
fig = px.box(
    data_frame=df, x='smoker', y='charges',
    facet_col='region', facet_col_wrap=2, color='sex',   
    width=700, height=700
)
fig.show()