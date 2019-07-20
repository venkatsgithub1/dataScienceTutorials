import numpy as np
def ecdf(data):
    # length of the data
    n = len(data)

    # sort the data (x)
    x= np.sort(data)

    # y-data
    y = np.arange(1, n+1) / n

    return x, y

from sklearn.datasets import load_iris
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

iris = load_iris()
df = pd.DataFrame(data=np.c_[iris.data, iris.target],
                 columns=iris.feature_names+['target'])

df['species']=df['target'].apply(lambda x:'setosa' if x==0 else('versicolor' if x==1 else 'virginica'))

print(df.head())
print(df.columns)

versicolor_petal_length = df[df['species']=='versicolor'].loc[:,'petal length (cm)']
setosa_petal_length = df[df['species']=='setosa'].loc[:,'petal length (cm)']
virginica_petal_length = df[df['species']=='virginica'].loc[:,'petal length (cm)']

x_vers, y_vers = ecdf(versicolor_petal_length)
x_set, y_set = ecdf(setosa_petal_length)
x_virg, y_virg = ecdf(virginica_petal_length)

plt.plot(x_set, y_set, marker='.', linestyle='none')
plt.plot(x_vers, y_vers, marker='.', linestyle='none')
plt.plot(x_virg, y_virg, marker='.', linestyle='none')

plt.legend(('setosa', 'versicolor', 'virginica'), loc='lower right')

plt.xlabel('petal length (cm)')
plt.ylabel('ECDF')

plt.show()
