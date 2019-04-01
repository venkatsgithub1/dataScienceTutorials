import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stocks.csv', header=0, index_col=0)

plt.subplot(2, 1, 1)

plt.xticks(rotation=45)

plt.title('AAPL: 2010 to 2011')

plt.plot(df.AAPL['2010':'2011'], color='blue')

plt.subplot(2, 1, 2)

plt.xticks(rotation=45)

plt.title('AAPL: 2009 to 2011')

plt.plot(df.AAPL['2009':'2011'], color='black')

plt.show()
