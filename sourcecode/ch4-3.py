df = pd.read_csv('./datasets/CO2_emissions/CO2_emissions.csv')
df.info()

# Seaborn scatterplot 그리기
fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)',
    data=df, hue='Vehicle Class', palette='bright',
    ax=ax
)

# 범례 위치 조절하기
fig, ax = plt.subplots()
sns.scatterplot(
    x='Fuel Consumption Comb (L/100 km)',
    y='CO2 Emissions(g/km)',
    data=df, hue='Vehicle Class', palette='bright',
    ax=ax
)
ax.legend(bbox_to_anchor=(1.01, 1.05))

# Plotly 그래프 범례 위치 조절
fig = px.scatter(
    df, x='Fuel Consumption Comb (L/100 km)', y='CO2 Emissions(g/km)',
    color='Vehicle Class', width=700, height=500
)
fig.update_layout(legend_x=1.2, legend_y=1)
fig.show()