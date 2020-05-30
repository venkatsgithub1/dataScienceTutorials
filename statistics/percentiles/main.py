from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


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
setosa_petal_length = df[df['species'] == 'setosa'].loc[:, 'petal length (cm)']
virginica_petal_length = df[df['species'] ==
                            'virginica'].loc[:, 'petal length (cm)']

percentiles = [2.5, 25, 50, 75, 97.5]
percentiles_vers = np.percentile(versicolor_petal_length, percentiles)
print(percentiles_vers)

x_vers, y_vers = ecdf(versicolor_petal_length)
plt.plot(x_vers, y_vers, '.')
plt.xlabel('petal length (cm)')
plt.ylabel('ECDF')

plt.plot(percentiles_vers, np.array(percentiles)/100,
         marker='D', color='red', linestyle='none')

plt.show()
