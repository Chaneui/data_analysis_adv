df = pd.read_csv('./datasets/ds_salaries/ds_salaries.csv')
companies = df.company_location.unique()[0:30]
df_10companies = df.loc[df['company_location'].isin(companies)]

fig, ax= plt.subplots()
sns.boxplot(
    x='company_location', y='salary_in_usd',
    data=df_10companies, ax=ax
)

# Matplotlib의 x축 라벨 회전
fig, ax= plt.subplots()
sns.boxplot(
    x='company_location', y='salary_in_usd',
    data=df_10companies, ax=ax
)
ax.tick_params(axis='x', labelrotation=90)

# Matplotlib의 x축 라벨 회전과 라벨 글씨 크기 수정
fig, ax= plt.subplots()
sns.boxplot(
    x='company_location', y='salary_in_usd',
    data=df_10companies, ax=ax
)
ax.tick_params(axis='x', labelrotation=90)
ax.tick_params(axis='both', which='major', labelsize=16)

# Plotly로 그린 boxplot의 x축 라벨 회전 및 글씨 크기 수정
fig = px.box(
    data_frame=df_10companies, x='company_location', y='salary_in_usd',
    width=500, height=400)
fig.update_xaxes(tickfont={'size':16}, tickangle=90)
fig.show()

# Matplotlib subplot 제목 설정하기
fig, ax= plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(x='company_size', y='salary_in_usd', data=df, ax=ax[0], order=['S','M','L'])
ax[0].set_title('company_size box plot', fontsize=16)

sns.histplot(x='salary_in_usd', data=df, ax=ax[1])
ax[1].set_title('salary histogram', fontsize=16)

pivot_df = df.pivot_table(
    index='company_size', columns='experience_level', values='salary_in_usd', aggfunc='mean'
)
sns.heatmap(pivot_df, ax=ax[2], annot=True)
ax[2].set_title('heatmap of\nexperience_level x company_size', fontsize=16)

# Matplotlib figure 제목 설정하기
fig, ax= plt.subplots(1, 3, figsize=(15, 5))

sns.boxplot(x='company_size', y='salary_in_usd', data=df, ax=ax[0], order=['S','M','L'])
ax[0].set_title('company_size box plot', fontsize=16)

sns.histplot(x='salary_in_usd', data=df, ax=ax[1])
ax[1].set_title('salary histogram', fontsize=16)

pivot_df = df.pivot_table(
    index='company_size', columns='experience_level', values='salary_in_usd', aggfunc='mean'
)
sns.heatmap(pivot_df, ax=ax[2], annot=True)
ax[2].set_title('heatmap of\nexperience_level x company_size', fontsize=16)

fig.suptitle('This is main title', fontsize=20)

# Plotly 그래프의 제목 설정하기
fig = px.box(
    data_frame=df, x='company_size', y='salary_in_usd',
    width=400, height=400,
    title='<b>company_size box plot</b>',
    category_orders={'company_size':['S','M','L']}
)
fig.update_layout({'title_font_size':20})
fig.show()

# Matplotlib 그래프의 grid 설정하기
fig, ax= plt.subplots()

sns.boxplot(
    x='company_size', y='salary_in_usd',
    data=df, ax=ax, order=['S','M','L']
)
ax.set_title('company_size box plot', fontsize=16)
ax.grid(axis='y')

# Plotly 그래프의 grid 설정하기
fig = px.box(
    df, x='company_size', y='salary_in_usd',
    height=400, width=400
)
fig.update_layout(yaxis={'showgrid':False})
fig.show()


# Matplotlib로 subplot 생성하기
fig, ax = plt.subplots(2, 2)
for idx in range(2):
    for jdx in range(2):
        ax[idx][jdx].set_xlabel('x_label')
        ax[idx][jdx].set_ylabel('y_label')
        ax[idx][jdx].set_title('title')
        
# Matplotlib로 생성한 subplot간 간격 설정하기
fig, ax = plt.subplots(2, 2)
for idx in range(2):
    for jdx in range(2):
        ax[idx][jdx].set_xlabel('x_label')
        ax[idx][jdx].set_ylabel('y_label')
        ax[idx][jdx].set_title('title')
        
plt.tight_layout()

# Plotly로 생성한 그래프의 subplot간 간격 조절하기
df = sns.load_dataset('tips')

fig = px.scatter(
    df, x='total_bill', y='tip',
    facet_row='sex', facet_col = 'time',
    width=600, height=600,
    facet_row_spacing=0.2, facet_col_spacing=0.1
)
fig.show()