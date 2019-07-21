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

samples = np.random.poisson(10, size=10000)

print('poisson:', np.mean(samples), np.std(samples))

n = [20, 100, 1000]
p = [0.5, 0.1, 0.01]

for i in range(3):
    samples_binomial = np.random.binomial(n[i], p[i], size=10000)

    print('binomial, n=', n[i], np.mean(
        samples_binomial), np.std(samples_binomial))
