import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

print(type(df.cyl))

plt.subplot(2, 1, 1)
sns.stripplot(x='cyl', y='hp', data=df, orient='h')

plt.subplot(2, 1, 2)
sns.stripplot(x='cyl', y='hp', data=df, jitter=True, size=3, orient='h')

plt.show()
