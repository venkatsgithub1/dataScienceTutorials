import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

plt.subplot(2, 1, 1)
sns.violinplot(x='cyl', y='hp', data=df)

plt.subplot(2, 1, 2)
sns.violinplot(x='cyl', y='hp', data=df, color='lightgray', inner=None)

sns.stripplot(x='cyl', y='hp', data=df, jitter=True, size=1.5)

plt.show()
