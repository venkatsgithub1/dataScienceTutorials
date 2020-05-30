from sklearn.metrics import f1_score, accuracy_score, precision_score, classification_report
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import glob
import pandas as pd


def gini(df_row, df):

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


def gini_split(row, df):
    value_counts_series = row.value_counts()

    count_list = []

    for key in value_counts_series.keys():
        count_list.append(value_counts_series.loc[key])

    no_0 = df[row == 0][20]
    no_1 = df[row == 1][20]

    gini0 = gini(no_0, df)
    gini1 = gini(no_1, df)

    gs = ((len(no_0)/len(df))*gini0)+((len(no_1)/len(df))*gini1)

    return gs


list_file_names = glob.glob('./data/*.csv')
list_file_names.sort()

for file_name in list_file_names:
    print("starting..........")
    print("file:", file_name)
    df_full = pd.read_csv(file_name, header=None)
    for i in range(len(df_full.columns)-1):
        print("column", i, "gini split value", gini_split(df_full[i], df_full))

    clf = DecisionTreeClassifier(class_weight=None, criterion='gini', max_depth=3, max_features=None, max_leaf_nodes=None,
                                 min_samples_leaf=5, min_samples_split=2, min_weight_fraction_leaf=0.0, presort=False, random_state=100, splitter='best')
    X = df_full.iloc[:, 1:20]
    y = df_full[20]
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)
    clf.fit(X_train, y_train)
    y_pred = clf.predict(X_test)
    print("score", clf.score)
    print("accuracy score", accuracy_score(y_test, y_pred)*100)
    print("f1 score", f1_score(y_test, y_pred, average=None))
    print("precision score", precision_score(
        y_test, y_pred, average=None))
    print("*****")
    print(classification_report(y_test, y_pred))
    print("ended")
