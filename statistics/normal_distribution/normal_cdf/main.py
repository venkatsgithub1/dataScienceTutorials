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


# normal distribution with mu = 20, std = 1 and 10000 samples
samples_std1 = np.random.normal(20, 1, size=10000)
# increasing deviation
samples_std2 = np.random.normal(20, 3, size= 10000)
samples_std3 = np.random.normal(20, 10, size=10000)

x_std1, y_std1 = ecdf(samples_std1)
x_std2, y_std2 = ecdf(samples_std2)
x_std3, y_std3 = ecdf(samples_std3)

sns.set()

_ = plt.plot(x_std1, y_std1, marker='.', linestyle='none')
_ = plt.plot(x_std2, y_std2, marker='.', linestyle='none')
_ = plt.plot(x_std3, y_std3, marker='.', linestyle='none')

_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))

plt.show()
