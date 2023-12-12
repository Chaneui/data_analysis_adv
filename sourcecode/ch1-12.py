df = pd.read_csv('datasets/APPL_price/APPL_price.csv')
df['Date'] = pd.to_datetime(df['Date'])
df = df.set_index('Date')

df.resample('7d').mean()