from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pandas as pd


def train_with(criterion, train_X, train_y):
    clf = DecisionTreeClassifier(
        criterion=criterion, random_state=100, max_depth=5, min_samples_leaf=5)

    clf.fit(train_X, train_y)

    return clf


def print_metrics(criterion, pred, actual):
    print(criterion + " metrics")
    print('accuracy score:')
    print(accuracy_score(actual, pred)*100)
    print('confusioin matrix:')
    print(confusion_matrix(actual, pred))
    print('classification report:')
    print(classification_report(actual, pred))


df = pd.read_csv('./data/1.csv')

# print(df.head())


X = df.values[:, :len(df.columns)-1]
y = df.values[:, -1]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.4, random_state=100)

clf = train_with('gini', X_train, y_train)
y_predicted = clf.predict(X_test)

print_metrics('gini', y_predicted, y_test)
