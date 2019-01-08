import datetime as dt 
import matplotlib.pyplot as plt 
from matplotlib import style
import pandas as pd 
import pandas_datareader.data as web

style.use('ggplot')

start = dt.datetime(2000,1,1)
end = dt.datetime(2018,12,31)

# df = web.DataReader('PNL.AS', 'yahoo', start, end)
#df.to_csv('POSTNL.csv')
df = pd.read_csv('POSTNL.csv', parse_dates=True, index_col=0) 
#print(df.head())

#df.plot()
# Ploting just one column
# df['Adj Close'].plot()
# plt.show()

# 100 moving average
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
#df.dropna(inplace=True)
#print(df.tail())

ax1 = plt.subplot2grid((6,1), (0,0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6,1), (5,0), rowspan=5, colspan=1, sharex=ax1)

ax1.plot(df.index, df['Adj Close'])
ax1.plot(df.index, df['100ma'])
ax2.bar(df.index, df['Volume'])

plt.show()