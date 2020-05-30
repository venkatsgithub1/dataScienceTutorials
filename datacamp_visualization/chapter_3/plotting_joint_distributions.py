import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv("auto-mpg.csv", header=0)

sns.jointplot(x='hp', y='mpg', data=df)

plt.show()
