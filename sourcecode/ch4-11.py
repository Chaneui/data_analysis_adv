df = sns.load_dataset('tips')

fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='size'
)

# seaborn color_palette 활용
color = sns.color_palette("light:#006d2c", as_cmap=True)

fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='size', palette=color
)

# seaborn color_palette 활용2
color = sns.color_palette("coolwarm", as_cmap=True)

fig, ax = plt.subplots()
sns.scatterplot(x='total_bill', y='tip', data=df, ax=ax,
               hue='size', palette=color)

color = sns.diverging_palette(250, 0, as_cmap=True)

# seaborn color_palette 활용3
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='size', palette=color
)

# seaborn palette 인자 활용
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='day', palette='bright'
)

# seaborn palette 인자 활용2
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='day', hue_order=['Thur','Fri','Sat','Sun'],
    palette=['black','cyan','purple','salmon']
)

# seaborn palette 인자 활용3
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='day', palette={'Thur':'black','Fri':'cyan','Sat':'purple','Sun':'salmon'}
)

# seaborn palette 인자 활용4
fig, ax = plt.subplots()
sns.scatterplot(
    x='total_bill', y='tip', data=df, ax=ax,
    hue='day', palette={'Thur':'#808000','Fri':'#0000FF','Sat':'#DDA0DD','Sun':'#BBF90F'}
)

# Seaborn Heatmap에서의 활용
df = sns.load_dataset('diamonds')
pivot = df.pivot_table(index='color', columns='clarity', values='price')
clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

fig, ax= plt.subplots(figsize=(8,6))
sns.heatmap(pivot[clarity_order], annot=True, fmt='.0f')

# Seaborn Heatmap에서의 camp 인자 활용
fig, ax= plt.subplots(figsize=(8,6))
sns.heatmap(
    pivot[clarity_order], annot=True, fmt='.0f',
    cmap=['black','darkgrey','lightgrey','white']
)

# Seaborn Heatmap에서 LinearSegmentedColormap 활용
from matplotlib.colors import LinearSegmentedColormap

color = LinearSegmentedColormap.from_list(
    'custom color',
    [(0, '#ffffff'),
    (0.5, '#ffffff'),
    (1, '#0000ff')], N=256
)

fig, ax= plt.subplots(figsize=(8,6))
sns.heatmap(
    pivot[clarity_order], annot=True, fmt='.0f',
    linewidth=0.5, linecolor='black', cmap=color
)

# Plotly 기본 color map
fig = px.colors.qualitative.swatches()
fig.show()

fig = px.colors.sequential.swatches_continuous()
fig.show()

fig = px.colors.diverging.swatches_continuous()
fig.show()

fig = px.colors.cyclical.swatches_continuous()
fig.show()

# Plotly에서의 color scale 활용
df = sns.load_dataset('tips')

fig = px.scatter(
    df, x='total_bill', y='tip', width=500, height=400,
    color='size', color_continuous_scale='balance'
)
fig.show()

# Plotly에서의 discrete sequence color map 활용
fig = px.scatter(
    df, x='total_bill', y='tip', width=500, height=400,
    color='day', color_discrete_sequence=px.colors.qualitative.Light24
)
fig.show()


# Plotly에서의 discrete color map 활용
fig = px.scatter(
    df, x='total_bill', y='tip', width=500, height=400,
    color='day', color_discrete_map={'Thur':'black','Fri':'cyan','Sat':'purple','Sun':'salmon'}
)
fig.show()

# Plotly에서의 discrete sequence color map 활용2
fig = px.scatter(
    df, x='total_bill', y='tip', width=500, height=400,
    color='day',
    color_discrete_sequence=[
        'rgb(255, 255, 255)',
        'rgb(0, 0, 0)',
        'rgb(128, 128, 128)',
        'rgb(64, 255, 192)'
    ]
)
fig.show()

# Plotly heatmap에서의 color map 활용
df = sns.load_dataset('diamonds')
pivot = df.pivot_table(index='color', columns='clarity', values='price')
clarity_order = ['I1','SI2','SI1','VS2','VS1','VVS2','VVS1','IF']

colors = ['black','darkgrey','lightgrey','white']
fig = px.imshow(
    pivot[clarity_order], width=500, height=400, text_auto='4d',
    color_continuous_scale=colors
)
fig.show()

# Plotly heatmap에서의 color map 활용2
fig = px.imshow(
    pivot[clarity_order], width=500, height=400, text_auto='4d',
)

fig.update_coloraxes(
    showscale=True,
    colorscale=[
        (0.0, '#FFFFFF'),
        (0.5, '#FFFFFF'),
        (1, '#0000FF'),
    ],
)

fig.show()