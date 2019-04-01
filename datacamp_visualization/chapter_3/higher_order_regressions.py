import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

print(df.columns)

hp = df.hp.values
mpg = df.mpg.values

plt.scatter(df['weight'], df['mpg'], label='data', color='red', marker='o')

sns.regplot(x='weight', y='mpg', data=df,
            label='order 1', color='blue', order=1, scatter=None)

sns.regplot(x='weight', y='mpg', data=df,
            label='order 2', color='green',
            order=2, scatter=None)

plt.show()
