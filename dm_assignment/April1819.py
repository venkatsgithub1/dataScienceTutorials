# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 20:47:58 2019

@author: Le Mercure
"""

import pandas as pd
import numpy as np

df = pd.read_csv('./data/1.csv', header=None)
# first column
for i in range(len(df.columns)-1):
    df_column = df[i]
    column_median = np.median(df_column)
    df[i]=df[i].apply(lambda x:1 if x>=column_median else 0)

head=df.head(125)    

def gini_value(faultinfo):
    global zero_values, one_values
    zero_values = df[df[0]==0]
    one_values = df[df[0]==1]
    
gini_value(df)
