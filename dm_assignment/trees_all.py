import pandas as pd
import numpy as np

# def calculate_entropy(df_row):
#     # get count of rows having 0
#     df_row.values

df = pd.read_csv('./data/2.csv', header=None)

for i in range(len(df.columns)):
    column_std = np.std(df[i])
    df[i] = df[i].apply(lambda x: 1 if x > column_std else 0)

# print(df.head())


def entropy(df_row):
    value_counts_series = df_row.value_counts()

    count_list = []

    for key in value_counts_series.keys():
        count_list.append(value_counts_series.loc[key])

    entropy = 0.0

    for data in count_list:
        prob = data/len(df)
        temp = prob*np.log2(prob)
        entropy += temp

    return -entropy


def entropy_for_attr(df_row, entropy_of_label):
    value_counts_series = df_row.value_counts()

    count_list = []

    for key in value_counts_series.keys():
        count_list.append(value_counts_series.loc[key])

    sum_of_entropies = 0.0

    for data in count_list:
        fraction = data/len(df)
        sum_of_entropies += (fraction*entropy(df_row))

    return entropy_of_label-sum_of_entropies


# value_counts_series = df.iloc[:, -1].value_counts()

# print(value_counts_series.keys())

# count_list = []

# for key in value_counts_series.keys():
#     count_list.append(value_counts_series.loc[key])

# print(count_list)

# count_list

# prob_list = []

# for data in count_list:
#     prob_list.append(data/len(df))

# print(sum([-x*np.log2(x) for x in prob_list]))
entropy_label = entropy(df.iloc[:, -1])
print(entropy_label)
for i in range(len(df.columns)-1):
    print(entropy_for_attr(df.iloc[:, i], entropy_label))
