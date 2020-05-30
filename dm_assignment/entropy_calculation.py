#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 22 21:28:06 2019

@author: ven
"""

import pandas as pd
import numpy as np


def find_entropy(dataframe, idx):
    labels = dataframe[20].unique()
    # for each label find entropy of 0's and 1's
    # p_0 = len(dataframe[dataframe[idx]==0])/len(dataframe[idx])
    # p_1 = len(dataframe[dataframe[idx]==1])/len(dataframe[idx])

    # return -(p_0*np.log2(p_0)+p_1*np.log2(p_1))
    counts_0 = []
    for label in labels:
        counts_0.append(len(df[(df[idx] == 0) & (df[20] == label)]))

    counts_1 = []
    for label in labels:
        counts_1.append(len(df[(df[idx] == 1) & (df[20] == label)]))

    entropy_array = np.array([counts_0, counts_1])
    sum_0 = np.sum(entropy_array[0])
    sum_1 = np.sum(entropy_array[1])

    # print(sum_0, sum_1, entropy_array)
    entropy_0s = 0

    # for 0s
    for i in range(0, len(labels)):
        prob = (entropy_array[0][i]) / (sum_0)
        if prob != 0:
            entropy_0s += prob * np.nan_to_num(np.log2(prob))
    entropy_0s *= (sum_0 / (sum_0 + sum_1))

    entropy_1s = 0

    # for 0s
    for i in range(0, len(labels)):
        prob = (entropy_array[1][i]) / (sum_1)
        if prob != 0:
            entropy_1s += prob * np.nan_to_num(np.log2(prob))

    entropy_1s *= (sum_1 / (sum_0 + sum_1))

    entropy = entropy_0s + entropy_1s

    return -entropy

    # for label in labels:
    #   p_0=len(dataframe[dataframe[idx]==0])


def find_entropy_label(dataframe):
    labels = dataframe[20].unique()
    prob_list = []
    for label in labels:
        prob_list.append(len(dataframe[dataframe[20] == label]) / len(dataframe[20]))
    entropy = 0
    for prob in prob_list:
        entropy += -((prob) * np.log2(prob))

    return entropy


def find_info_gain(dataframe):
    entropy_of_label = find_entropy_label(df)
    # print("--info gains--")
    ig_list = []
    for column in range(0, len(dataframe.columns)-1):
        # print("column", column, find_entropy(df, column), entropy_of_label)
        gain = entropy_of_label - find_entropy(df, column)
        if gain == "":
            gain = 0
        ig_list.append(gain)
    return ig_list


writer1 = pd.ExcelWriter('2018HT12007' + '_infogain.xlsx', engine='xlsxwriter')

for i in range(1, 57):
    print("file", i)
    df = pd.read_csv('./data/{}.csv'.format(i), header=None)
    for j in range(0, len(df.columns) - 1):
        df[j] = df[j].apply(lambda x: 1 if x > np.std(df[j]) else 0)
    df = pd.DataFrame({"Information gain for {}.csv".format(i): find_info_gain(df)})
    df.to_excel(writer1, sheet_name="{}.csv".format(i), index=None)

writer1.save()
