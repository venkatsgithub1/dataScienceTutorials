import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


def ecdf(data):
    # length of the data
    n = len(data)

    # sort the data (x)
    x = np.sort(data)

    # y-data
    y = np.arange(1, n+1) / n

    return x, y


# setting seaborn style
sns.set()

# n_defaults contains success of binomial trails, where
# for example a coin is tossed 100 times and how many times the
# probability 0.05 occurred is returned, this same thing
# is done for 10000 times.
n_defaults = np.random.binomial(n=100, p=0.05, size=10000)

bins = np.arange(0, max(n_defaults)+1+1)-0.5

_ = plt.hist(n_defaults, bins=bins, normed=True)

_ = plt.xlabel('number of defaults out of 100 loans')
_ = plt.ylabel('PMF')

plt.show()
