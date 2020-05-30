import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stocks.csv', header=0, index_col=0)

df.index = pd.to_datetime(df.index)

aapl = df.AAPL

view_1 = aapl['2007-11':'2008-04']

plt.subplot(2, 1, 1)
plt.xticks(rotation=45)
plt.title('AAPL: Nov. 2007 to Apr. 2008')
plt.plot(view_1, color='red')

view_2 = aapl['2008-01']

plt.subplot(2, 1, 2)
plt.xticks(rotation=45)
plt.title('AAPL: Jan. 2008')
plt.plot(view_2, color='green')

plt.show()
