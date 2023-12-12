df = pd.read_csv('./datasets/CO2_emissions/CO2_emissions.csv')

fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', data=df, ax=ax, hue='Fuel Type'
)
ax.text(
    x=10, y=130,
    s='fuel type ethanol emits less CO2',
    fontdict={'fontsize':12, 'weight':'bold'}
)

# 상대 좌표 사용
fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', data=df, ax=ax, hue='Fuel Type'
)
ax.text(
    x=0.3, y=0.12,
    s='fuel type ethanol emits less CO2',
    fontdict={'fontsize':12, 'weight':'bold'},
    transform=ax.transAxes
)

# annotation 메서드를 이용한 화살표 사용
fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', data=df, ax=ax, hue='Fuel Type'
)
ax.annotate(
    text='ethanol is efficient', xy=(26, 400),
    xytext=(21,310), arrowprops={'color':'black', 'width':1}
)

# annotation 메서드에 상대좌표 사용
fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', data=df, ax=ax, hue='Fuel Type'
)
ax.annotate(
    text='ethanol is efficient', xy=(0.95, 0.7),
    xytext=(0.73, 0.5), arrowprops={'color':'black', 'width':1},
    xycoords=ax.transAxes
)

# Plotly annotation
fig = px.scatter(
    df, x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)', width=500, height=400,
    color='Fuel Type'
)
fig.add_annotation(
    x=20, y=130, text='<b>fuel type ethanol emits less CO2</b>',
    showarrow=False
)
fig.add_annotation(
    x=0.9, xref='x domain', y=0.75, yref='y domain', text='ethanol is efficient',
    showarrow=True, arrowhead=2
)
fig.show()