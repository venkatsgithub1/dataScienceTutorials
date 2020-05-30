import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

plt.subplot(2, 1, 1)
sns.swarmplot(x='cyl', y='hp', data=df, orient='h')

plt.subplot(2, 1, 2)
sns.swarmplot(x='hp', y='cyl', data=df, hue='origin', orient='h')

plt.show()
