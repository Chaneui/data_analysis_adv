df = pd.read_csv('./datasets/medical_cost/medical_cost.csv')
df.head()

# age_bin 변수 그룹화 후 pivot table 생성 및 Seaborn heatmap 시각화
age_bin_list = np.arange(10, 80, 10)
df['age_bin'] = pd.cut(df['age'], bins=age_bin_list)

pivot_df = df.pivot_table(
    index='age_bin', columns='region', values='charges', aggfunc='median'
)

fig, ax = plt.subplots()
sns.heatmap(pivot_df, ax=ax, annot=True)

# Seaborn heatmap의 annotation 포멧 변경
fig, ax = plt.subplots()
sns.heatmap(pivot_df, ax=ax, annot=True, fmt='.2e')

# Seaborn heatmap의 color map 활용
fig, ax = plt.subplots()
sns.heatmap(
    pivot_df, ax=ax, annot=True, fmt='.2e',
    vmax=16000, vmin=0, cmap='RdBu'
)

# Plotly heatmap
fig = px.imshow(
    pivot_df, x=pivot_df.columns, y=pivot_df.index.astype('str'),
    text_auto='.2e', width=400, height=400
)
fig.show()

# Plotly heatmap의 color map 활용
fig = px.imshow(
    pivot_df, x=pivot_df.columns, y=pivot_df.index.astype('str'),
    text_auto='.2e',width=400, height=400,
    color_continuous_scale='RdBu'
)
fig.show()