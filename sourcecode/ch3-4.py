df = pd.read_csv('./datasets/EV_charge/EV_charge.csv')

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)

# Seaborn stripplot과 boxplot 동시 활용
fig, ax = plt.subplots()
sns.stripplot(x='weekday', y='kwhTotal', data=df, ax=ax, color='grey', alpha=0.4)
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)

# Seaborn swarmplot과 boxplot 동시 활용
fig, ax = plt.subplots()
sns.swarmplot(x='weekday', y='kwhTotal', data=df, ax=ax, color='grey', alpha=0.4)
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax)

# Seaborn boxplot의 범주형 x축 순서 수정
weekday_order = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']

fig, ax = plt.subplots()
sns.boxplot(x='weekday', y='kwhTotal', data=df, ax=ax, order=weekday_order)

# Seaborn boxplot의 변수 그룹별 box 나누기
fig, ax = plt.subplots()
sns.boxplot(
    x='weekday', y='kwhTotal',
    data=df, ax=ax, order=weekday_order, hue='platform'
)

# Plotly boxplot
fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal',
    width=500, height=400
)
fig.show()

# Plotly boxplot point 추가
fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal',
    width=500, height=400, points='all'
)
fig.show()

# Plotly boxplot의 범주형 x축 순서 수정
weekday_order = {'weekday': ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}
fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal',
    width=500, height=400,
    category_orders=weekday_order
)
fig.show()

# Plotly boxplot의 변수 그룹별 box 나누기
weekday_order = {'weekday': ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']}
fig = px.box(
    data_frame=df, x='weekday', y='kwhTotal',
    width=500, height=400,
    category_orders=weekday_order, color='platform'
)
fig.show()