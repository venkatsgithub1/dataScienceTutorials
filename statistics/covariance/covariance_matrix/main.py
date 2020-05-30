from sklearn.datasets import load_iris
import pandas as pd
import numpy as np


def ecdf(data):
    # length of the data
    n = len(data)

    # sort the data (x)
    x = np.sort(data)

    # y-data
    y = np.arange(1, n+1) / n

    return x, y


iris = load_iris()
df = pd.DataFrame(data=np.c_[iris.data, iris.target],
                  columns=iris.feature_names+['target'])

df['species'] = df['target'].apply(
    lambda x: 'setosa' if x == 0 else('versicolor' if x == 1 else 'virginica'))

print(df.head())
print(df.columns)

versicolor_petal_length = df[df['species'] ==
                             'versicolor'].loc[:, 'petal length (cm)']
versicolor_petal_width = df[df['species'] ==
                            'versicolor'].loc[:, 'petal width (cm)']

covariance_matrix = np.cov(versicolor_petal_length, versicolor_petal_width)

print(covariance_matrix)

petal_cov = covariance_matrix[0, 1]

print(petal_cov)