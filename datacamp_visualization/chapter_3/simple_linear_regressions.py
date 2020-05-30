import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

print(df.columns)

hp = df.hp.values
mpg = df.mpg.values
weight = df.weight.values

sns.lmplot(x='weight', y='hp', data=df)

plt.show()
