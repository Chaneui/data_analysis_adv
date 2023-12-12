# Matplotlib로 2개의 축을 가지는 그래프 생성
df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])

fig, ax = plt.subplots()
ax2 = ax.twinx()
sns.lineplot(x='Date', y='Close', data=df, ax=ax, color='red')
sns.lineplot(x='Date', y='Volume', data=df, ax=ax2, color='blue')

ax.tick_params(axis='y', labelcolor='red')
ax.yaxis.label.set_color('red')

ax2.tick_params(axis='y', labelcolor='blue')
ax2.yaxis.label.set_color('blue')

ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

# matplotlib의 축 색깔 변경
ax.yaxis.label.set_color('red')
ax2.yaxis.label.set_color('blue')

# ABNB_stock 데이터셋에 파생 변수 생성
df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['High-Low'] = df['High'] - df['Low']

# Matplotlib로 3개의 축을 가지는 그래프 생성
fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

ax2 = ax.twinx()
ax3 = ax.twinx()

    # 세 번째 y축(ax3)을 그래프의 바깥으로 옮깁니다.
ax3.spines.right.set_position(("axes", 1.2))

sns.lineplot(x='Date', y='Close', data=df, ax=ax, color='red')
sns.lineplot(x='Date', y='Volume', data=df, ax=ax2, color='blue')
sns.lineplot(x='Date', y='High-Low', data=df, ax=ax3, color='green')

ax.yaxis.label.set_color('red')
ax2.yaxis.label.set_color('blue')
ax3.yaxis.label.set_color('green')

tkw = dict(size=4, width=1.5)
ax.tick_params(axis='y', colors='red', **tkw)
ax2.tick_params(axis='y', colors='blue', **tkw)
ax3.tick_params(axis='y', colors='green', **tkw)
ax.tick_params(axis='x', **tkw)

ax.xaxis.set_major_formatter(mpl.dates.ConciseDateFormatter(ax.xaxis.get_major_locator()))

# Plotly를 이용한 2중 축 그래프 그리기
from plotly.subplots import make_subplots
df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['High-Low'] = df['High'] - df['Low']

fig = make_subplots(specs=[[{"secondary_y": True}]])

subfig1 = px.line(df, x='Date', y='Close')
subfig1.update_traces(line_color='red')
subfig2 = px.line(df, x='Date', y='Volume')
subfig2.update_traces(line_color='blue')

subfig2.update_traces(yaxis='y2')

fig.add_traces(subfig1.data + subfig2.data)

fig.layout.xaxis.title = 'Date'
fig.layout.yaxis.title = 'Close'
fig.layout.yaxis2.title = 'Volume'
fig.layout.yaxis.color = 'red'
fig.layout.yaxis2.color = 'blue'

fig.update_layout(width=500, height=400)
fig.show()

# Plotly를 이용한 3중 축 그래프 그리기
import plotly.graph_objects as go

df = pd.read_csv('./datasets/ABNB_stock/ABNB_stock.csv')
df['Date'] = pd.to_datetime(df['Date'])
df['High-Low'] = df['High'] - df['Low']

fig = make_subplots()
fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['Close'], name='Close',
        mode='lines', yaxis='y', line={'color':'red'},
    )
)

fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['Volume'], name='Volume',
        mode='lines', yaxis='y2', line={'color':'blue'},
    )
)

fig.add_trace(
    go.Scatter(
        x=df['Date'], y=df['High-Low'], name='High-Low',
        mode='lines', yaxis='y3', line={'color':'green'},
    )
)

fig.update_layout(
    yaxis = dict(title = "Close"),
    yaxis2 = dict(
        position = 1, title = "Volume",
        side = "right", anchor = "free", overlaying = "y"
        ),
    yaxis3 = dict(
        title = "High-Low", side = "right", anchor = "x",
        overlaying = "y"
    ),
    xaxis = dict(title = "Date", domain = [.1, .85]),
    width=600, height=400
)

fig.layout.yaxis.color = 'red'
fig.layout.yaxis2.color = 'blue'
fig.layout.yaxis3.color = 'green'

fig.show()