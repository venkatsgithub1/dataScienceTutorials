# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 23:25:45 2019

@author: Le Mercure
"""

import pandas as pd

df = pd.read_csv('./3)cancer.csv')

from sklearn import preprocessing

le = preprocessing.LabelEncoder()

le.fit(df['Occupation'].unique())

print(le.classes_)

df['Occupation']=le.transform(df['Occupation'])

from matplotlib import pyplot as plt

plt.scatter(df['Smoke.Index'], df['Cancer.Index'])

plt.show()

plt.hist(df['Occupation'], color="violet")

plt.show()

import seaborn as sns

sns.lmplot(data=df, x='Occupation', y='Cancer.Index')

plt.show()