#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 18:36:36 2019

@author: ven
"""

import pandas as pd

df=pd.read_csv("./data/1.csv", header=None)

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(criterion='entropy')

from sklearn.model_selection import KFold

from sklearn.metrics import accuracy_score, f1_score

X=df.iloc[:,[0,20]]
y=df.iloc[:,20]

kf=KFold(n_splits=10)
for train_index, test_index in kf.split(X):
    print("TRAIN:", train_index, "TEST:", test_index)
    X_train, X_test = X[train_index], X[test_index]
    y_train, y_test = y[train_index], y[test_index]
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print(accuracy_score(y_test, y_pred))
    print(f1_score(y_test, y_pred))