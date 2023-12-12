df = pd.read_csv('./datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

g = sns.FacetGrid(df, sharex=False, sharey=False, col='inspection_step', aspect=1.6)
g.map_dataframe(sns.scatterplot, x='date', y='value')

# 함수를 이용한 facetgrid mapping
import matplotlib as mpl
def custom(lower_spec, target, upper_spec, **kws):
    ax = plt.gca()
    
    ax.axhline(lower_spec.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(target.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(upper_spec.iloc[-1], color='red', linewidth=0.5)
    
    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    
g.map(custom, 'lower_spec', 'target', 'upper_spec')

# for 문을 이용한 facetgrid mapping 
g = sns.FacetGrid(df, sharex=False, sharey=False, col='inspection_step', aspect=1.6)
g.map_dataframe(sns.scatterplot, x='date', y='value')

for ax in g.axes.flat:
    inspection_step = ax.get_title()[-1]
    temp_df = df.loc[df['inspection_step'] == inspection_step]
    
    ax.axhline(temp_df['lower_spec'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['upper_spec'].iloc[-1], color='red', linewidth=0.5)
    ax.axhline(temp_df['target'].iloc[-1], color='red', linewidth=0.5)
    
    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    
# 함수를 이용한 facetgrid mapping 활용
import matplotlib.transforms as transforms

g = sns.FacetGrid(df, sharex=False, sharey=False, col='inspection_step', aspect=1.6)
g.map_dataframe(sns.scatterplot, x='date', y='value')

def custom(value, lower_spec, target, upper_spec, **kws):
    ax = plt.gca()
    
    ax.axhline(lower_spec.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(target.iloc[-1], color='red', linewidth=0.5)
    ax.axhline(upper_spec.iloc[-1], color='red', linewidth=0.5)
    
    ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))
    
    mean = value.mean()
    ax.axhline(mean, color='blue', linestyle='--', linewidth=2)
    
    trans = transforms.blended_transform_factory(ax.transAxes, ax.transData)
    ax.text(x=0.02, y=mean, s='mean: {:.1f}'.format(mean),
           fontdict={'fontsize':12, 'weight':'bold'}, bbox={'facecolor':'white'},
            transform=trans, ha='left')
    
g.map(custom, 'value', 'lower_spec', 'target', 'upper_spec')

# Plotly에서의 활용
df = pd.read_csv('./datasets/product_inspection/product_inspection.csv')
df['date'] = pd.to_datetime(df['date'])

fig = px.scatter(df, x='date', y='value', facet_col='inspection_step')
print(fig.layout.annotations)

# For 문을 이용한 plotly에서의 facet mapping
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
    
fig.update_yaxes(matches=None)
fig.update_yaxes(showticklabels=True)
fig.show()

# For 문을 이용한 plotly에서의 facet mapping 활용
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
    
    med = df.query('inspection_step == @step')['value'].median()
    fig.add_hline(
        y=med,
        line_color='black', line_width=3, line_dash='dot', row=1, col=idx+1
    )
    
    fig.add_annotation(
        text='median: {:.1f}'.format(med),
        showarrow=False, bordercolor='black', borderwidth=1, bgcolor='rgb(256,256,256)',
        x=0.02, y=med, xref='x domain', row=1, col=idx+1,
    )
    
fig.update_yaxes(matches=None)
fig.update_yaxes(showticklabels=True)
fig.show()