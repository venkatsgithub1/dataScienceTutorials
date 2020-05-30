import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stocks.csv', header=0, index_col=0)

df.index = pd.to_datetime(df.index)

aapl = df.AAPL

view = aapl['2007-11':'2008-04']

plt.plot(aapl)

plt.xticks(rotation=45)
plt.title('AAPL:2000-2011')

plt.axes([0.25, 0.5, 0.35, 0.35])

plt.plot(view, color='red')
plt.xticks(rotation=45)
plt.title('2007/11-2008/04')
plt.show()
