import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('stocks.csv', header=0)

print(df.columns)

plt.plot(df.AAPL, color='blue', label='AAPL')

plt.plot(df.IBM, color='green', label='IBM')

plt.plot(df.CSCO, color='red', label='CSCO')

plt.plot(df.MSFT, color='magenta', label='MSFT')

plt.show()
