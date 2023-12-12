df = sns.load_dataset('tips')

fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax)

# Seaborn histplot의 bin size 수정
fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, bins=30)

# Seaborn histplot의 bin size 수정2
fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, binwidth=2)

# Seaborn histplot의 특정 변수 그룹별 막대 나누기
fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, hue='time')

# Seaborn histplot의 multiple 인자 활용
fig, ax = plt.subplots()
sns.histplot(df, x='total_bill', ax=ax, hue='time', multiple='stack')

# Ploty histogram
df = sns.load_dataset('tips')

fig = px.histogram(data_frame=df, x='total_bill', width=450)
fig.show()

# Plotly histplot의 bin size 수정
fig = px.histogram(
    data_frame=df, x='total_bill', width=450, nbins=20
)
fig.show()

# Plotly histplot의 특정 변수 그룹별 막대 나누기
fig = px.histogram(
    data_frame=df, x='total_bill', width=450,
    color='time', barmode='overlay'
)

# Plotly histplot의 특정 변수 그룹별 막대 나누기2
fig = px.histogram(
    data_frame=df, x='total_bill', width=450, color='time'
)
fig.show()