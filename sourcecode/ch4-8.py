# 데이터 로드 및 spec_out 파생변수 생성
df = pd.read_csv('./datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

df['spec_out'] = (df['value'] > df['upper_spec']) | (df['value'] < df['lower_spec'])

# Seaborn을 이용한 조건문 활용 facetgrid mapping
g = sns.FacetGrid(df, sharex=False, sharey=False, col='inspection_step', aspect=1.6)
g.map_dataframe(sns.scatterplot, x='date', y='value')

def custom(value, lower_spec, target, upper_spec, **kws):
    ax = plt.gca()
    
    ax.axhline(lower_spec.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(target.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(upper_spec.iloc[-1], color='red', linewidth=0.5)
    
    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    
def if_spec_out(spec_out, **kws):
    if spec_out.sum() > 0:
        ax = plt.gca()
        spines = ['left','bottom']
        for spine in spines:
            ax.spines[spine].set_color('blue')
            ax.spines[spine].set_linewidth(3)
        
g.map(custom, 'value', 'lower_spec', 'target', 'upper_spec')
g.map(if_spec_out, 'spec_out')

# Seaborn을 이용한 조건문 활용 facetgrid mapping2
g = sns.FacetGrid(df, sharex=False, sharey=False, col='inspection_step', aspect=1.6)
g.map_dataframe(sns.scatterplot, x='date', y='value')

for ax in g.axes.flat:
    title = ax.get_title()[-1]
    temp_df = df.query('inspection_step == @title')
    
    ax.axhline(temp_df['lower_spec'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['target'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['upper_spec'].iloc[-1], color='red', linewidth=0.5)
    
    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    
    spec_out_df = temp_df.query('spec_out != 0')
    if len(spec_out_df) > 0:
        for idx in range(len(spec_out_df)):
            ax.annotate(
                xy=(spec_out_df.iloc[idx]['date'], spec_out_df.iloc[idx]['value']),
                xytext=(spec_out_df.iloc[idx]['date'], spec_out_df.iloc[idx]['value']*1.01),
                text='spec_out', arrowprops={'color':'red', 'width':2}, color='red', weight='bold'
            )
                        
# Plotly를 이용한 조건문 활용 facetgrid mapping
fig = px.scatter(df, x='date', y='value', facet_col='inspection_step', facet_col_spacing=0.05)

for idx in range(df['inspection_step'].nunique()):
    step = fig.layout.annotations[idx].text.split('=')[1]
    fig.add_hline(
        y=df.query('inspection_step == @step')['lower_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['upper_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['target'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    
    if df.query('inspection_step == @step')['spec_out'].sum() > 0:
        fig.update_xaxes(showline=True, linecolor='black', linewidth=3, mirror=True, row=1, col=idx+1)
        fig.update_yaxes(showline=True, linecolor='black', linewidth=3, mirror=True, row=1, col=idx+1)
    
fig.update_yaxes(matches=None)
fig.update_yaxes(showticklabels=True)
fig.show()

# Plotly를 이용한 조건문 활용 facetgrid mapping2
fig = px.scatter(df, x='date', y='value', facet_col='inspection_step', facet_col_spacing=0.05)

for idx in range(df['inspection_step'].nunique()):
    step = fig.layout.annotations[idx].text.split('=')[1]
    fig.add_hline(
        y=df.query('inspection_step == @step')['lower_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['upper_spec'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    fig.add_hline(
        y=df.query('inspection_step == @step')['target'].iloc[-1],
        line_color='red', line_width=0.5, row=1, col=idx+1
    )
    
    spec_out_df = df.query('inspection_step == @step and spec_out != 0')
    if len(spec_out_df) > 0:
        for jdx in range(len(spec_out_df)):
            fig.add_annotation(
                text='spec out', x=spec_out_df.iloc[jdx]['date'], y=spec_out_df.iloc[jdx]['value'],
                row=1, col=idx+1, arrowcolor='red', font={'color':'red'}
            )
                
    
fig.update_yaxes(matches=None)
fig.update_yaxes(showticklabels=True)
fig.show()