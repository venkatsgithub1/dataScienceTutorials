import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from scipy.stats.stats import pearsonr
import math
from sklearn import linear_model
from sklearn.model_selection import train_test_split

df = pd.read_csv('./8)heigt-weight.csv')

"""
Method takes X - independent variable, y - dependent variable,
splits data into training and testing data and returns
mean absolute error, mean squared error, r2 score
"""


def train_and_check_performance(inix, iniy, label_string):
    train_x, test_x, train_y, test_y = train_test_split(inix, iniy)

    lr = linear_model.LinearRegression()

    lr.fit(train_x, train_y)

    pred_y = lr.predict(test_x)
    
    plt.title('height vs weight for '+label_string)
    plt.scatter(test_x, test_y)
    plt.scatter(test_x, pred_y, color='red')
    plt.show()

    mse = mean_squared_error(pred_y, test_y)

    r2score = r2_score(test_y, pred_y)

    mae = mean_absolute_error(test_y, pred_y)

    return mae, math.sqrt(mse), r2score


# getting male data.
male_df = df[df['Gender'] == 'Male']

# getting female data.
female_df = df[df['Gender'] == 'Female']

# using seaborn lmplot to draw lmplot for linear regression for male data.
sns.lmplot(data=male_df, x='Height', y='Weight', hue='Gender')
# using seaborn lmplot to draw lmplot for linear regression for female data.
sns.lmplot(data=female_df, x='Height', y='Weight', hue='Gender')
# using seaborn lmplot to draw lmplot for linear regression for full data.
sns.lmplot(data=df, x='Height', y='Weight', hue='Gender')
# showing graph.
plt.show()

plt.xlabel('Height')
plt.ylabel('Weight')
plt.scatter(male_df['Height'], male_df['Weight'], color='green')
plt.scatter(female_df['Height'], female_df['Weight'], color='red')
plt.title('Height vs Weight')
plt.show()

# getting pearson correlation coefficient.
r = pearsonr(df['Height'], df['Weight'])

# getting height and weight columns.
X = male_df.loc[:, ['Height']]
y = male_df.loc[:, ['Weight']]

# calling a method to apply linear regression and calculating root mean square error, r2 score for male data.
mae, retrmse, retr2 = train_and_check_performance(X, y, 'male data')

X = female_df.loc[:, ['Height']]
y = female_df.loc[:, ['Weight']]

# calling a method to apply linear regression and calculating root mean square error, r2 score for female data.
maef, retfrmse, retfr2 = train_and_check_performance(X, y, 'female data')
