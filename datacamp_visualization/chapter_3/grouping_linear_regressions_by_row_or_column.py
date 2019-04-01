import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

print(df.columns)

sns.lmplot(x='weight', y='hp', col='origin', data=df)

plt.tight_layout()
plt.show()