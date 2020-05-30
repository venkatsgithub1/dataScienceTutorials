import numpy as np
from sklearn.decomposition import PCA
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale

data=pd.read_csv('./5)Folds5x2_pp.csv')

X=data.values

X = scale(X)

pca=PCA(n_components=5)

pca.fit(X)

var=pca.explained_variance_ratio_

pca_var = np.round(pca.explained_variance_ratio_*100, decimals=4)

pca_cum_sum = np.cumsum(np.round(pca.explained_variance_ratio_, decimals=4)*100)

print(pca_cum_sum, "cum sum")
print(pca_var, "pca var")

plt.plot(pca_cum_sum)

plt.show()

pca=PCA(n_components=2)
pca.fit(X)
X_2=pca.fit_transform(X)

print(X_2)