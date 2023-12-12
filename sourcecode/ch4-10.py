df = pd.read_csv('./datasets/Covid19-India/Covid19-India.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.loc[df.region == 'Maharashtra']

fig, ax = plt.subplots()
sns.lineplot(x='date', y='confirmed', data=df, ax=ax)
ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

# y축 로그 변환
fig, ax = plt.subplots()
sns.lineplot(x='date', y='confirmed', data=df, ax=ax)
ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
ax.set_yscale('log')

# Plotly에서의 활용
fig = px.line(
    df, x='date', y='confirmed', width=500, height=400, log_y=True
)
fig.show()