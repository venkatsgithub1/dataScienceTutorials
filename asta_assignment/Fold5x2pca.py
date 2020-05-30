import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

df = pd.read_csv('./6)FuelEfficiency.csv')

print(df.head())

print(df.shape)

scaled_df = preprocessing.scale(df.T)

print(scaled_df)

principal_component_analysis = PCA()

principal_component_analysis.fit(scaled_df)
pca_data = principal_component_analysis.transform(scaled_df)

print(pca_data, "pca data")

pca_variance = np.round(principal_component_analysis.explained_variance_ratio_ * 100, decimals=2)

print(pca_variance, "variance")

labels = ['PC' + str(x) for x in range(1, len(pca_variance) + 1)]

plt.bar(x=range(1, len(pca_variance) + 1), height=pca_variance, tick_label=labels)
plt.ylabel('Percentage of explained variance')
plt.xlabel('Principal Component')
plt.title('Scree plot')
plt.show()

pca_df = pd.DataFrame(pca_data, index=df.columns, columns=labels)

print(pca_df)

print(principal_component_analysis.components_.shape, "top principal component items")
