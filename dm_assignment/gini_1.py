import pandas as pd
import numpy as np

# def calculate_entropy(df_row):
#     # get count of rows having 0
#     df_row.values

df = pd.read_csv('./data/1.csv', header=None)

for i in range(len(df.columns)-1):
    # print(i, np.median(df[i]))
    df[i] = df[i].apply(
        lambda x: 1 if x >= np.median(df[i]) else 0)

# print(df.head())


def gini(df_row):

    value_counts_series = df_row.value_counts()

    count_list = []

    # print(value_counts_series.keys(), "data")

    for key in value_counts_series.keys():
        count_list.append(value_counts_series.loc[key])

    # print(count_list)

    ginit = 0.0

    for data in count_list:
        prob = data/len(df)
        temp = prob**2
        ginit += temp

    return 1-ginit


def gini_split(row):
    value_counts_series = row.value_counts()

    count_list = []

    for key in value_counts_series.keys():
        count_list.append(value_counts_series.loc[key])

    no_0 = df[row == 0][20]
    no_1 = df[row == 1][20]

    gini0 = gini(no_0)
    gini1 = gini(no_1)

    gs = ((len(no_0)/len(df))*gini0)+((len(no_1)/len(df))*gini1)

    return gs


print('beginning to calculate')
for i in range(0, len(df.columns)-1):
    print(i)
    print(gini_split(df[i]))
