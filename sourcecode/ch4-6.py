df = pd.read_csv('./datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

df = df.query('inspection_step == "A"')

fig, ax = plt.subplots()
sns.scatterplot(x='date', y='value', data=df, ax=ax)
ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

# 수평선 그리기
fig, ax = plt.subplots()
sns.scatterplot(x='date', y='value', data=df, ax=ax)
ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

ax.axhline(df['lower_spec'].iloc[-1], color='red', linewidth=0.5)
ax.axhline(df['target'].iloc[-1], color='red', linewidth=0.5)
ax.axhline(df['upper_spec'].iloc[-1], color='red', linewidth=0.5)

# Plotly scatter 수평선 그리기
fig = px.scatter(df, x='date', y='value', width=500, height=400)
fig.add_hline(df['lower_spec'].iloc[-1], line_color='red', line_width=0.5)
fig.add_hline(df['target'].iloc[-1], line_color='red', line_width=0.5)
fig.add_hline(df['upper_spec'].iloc[-1], line_color='red', line_width=0.5)
fig.show()