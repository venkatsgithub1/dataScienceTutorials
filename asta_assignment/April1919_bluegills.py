# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 07:49:56 2019

@author: Le Mercure
"""

import pandas as pd

df=pd.read_csv('./2)BlueGills.csv')

from matplotlib import pyplot as plt
import seaborn as sns

sns.lmplot(data=df, x='age', y='length')
plt.show()

from sklearn.model_selection import train_test_split

X=df.loc[:,['age']]
y=df.loc[:,['length']]

trainX, testX, trainy, testy = train_test_split(X, y)

from sklearn import linear_model

lr = linear_model.LinearRegression()

lr.fit(trainX, trainy)

predy=lr.predict(testX)

from sklearn.metrics import mean_squared_error
import math

root_mean_squared_error = math.sqrt(mean_squared_error(testy, predy))