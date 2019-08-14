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


def perform_beronaulli_trails(n, p):
    # n = number of trails, p = success probability
    n_success = 0
    for i in range(n):
        # creating random number
        random_number = np.random.random()

        # if random number is less than p, we add 1 to success
        if random_number < p:
            n_success += 1

    # returning success number count
    return n_success


# setting seed
np.random.seed(42)

# creating empty array of size 1000
n_defaults = np.empty(1000)

# looping 1000 times and testing for beronaulli trails 100 times for each iteration.
for i in range(1000):
    # out of 100 iterations of beronaulli trails how many times is experiment a
    # success ?
    n_defaults[i] = perform_beronaulli_trails(100, 0.05)


# setting seaborn style
sns.set()

x, y = ecdf(n_defaults)

plt.plot(x, y, marker='.', linestyle='none')
plt.xlabel('number of defaults out of 100')
plt.ylabel('CDF')

plt.show()
