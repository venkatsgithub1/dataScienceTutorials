import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("auto-mpg.csv", header=0)

# print(df.head())

hp = df.hp.values
mpg = df.mpg.values

plt.hist2d(hp, mpg, bins=(20, 20), range=(
    (np.min(hp), np.max(hp)), (np.min(mpg), np.max(mpg))))

plt.colorbar()
plt.xlabel("Horse Power (HP)")
plt.ylabel("Miles per Gallon (mpg)")
plt.title("hist2d plot")
plt.show()
