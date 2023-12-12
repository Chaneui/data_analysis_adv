df = pd.read_csv('./datasets/global_internet_users/global_internet_users.csv')
entities = ['China', 'India', 'Finland']
df = df.loc[df['Entity'].isin(entities)]

fig, ax = plt.subplots()
sns.lineplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity'
)

# seaborn line plot과 scatterplot을 한번에 그리기
fig, ax = plt.subplots()
sns.lineplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity'
)
sns.scatterplot(
    x='Year', y='No. of Internet Users',
    data=df, ax=ax, hue='Entity', legend=False
)

# Plotly lineplot
fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, color='Entity'
)
fig.show()

# Plotly lineplot의 line dash 인자 활용
fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400, line_dash='Entity'
)
fig.show()

# Plotly lineplot의 line dash과 symbol 인자 동시 활용
fig = px.line(
    data_frame=df, x='Year', y='No. of Internet Users',
    width=400, height=400,
    color='Entity', symbol='Entity'
)
fig.show()