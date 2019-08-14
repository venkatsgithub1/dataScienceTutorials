import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns

# setting seaborn style
sns.set()

# set seed
np.random.seed(42)

# creating an empty array of size 10000
random_numbers = np.empty(10000)

# inserting 10000 random numbers
for i in range(10000):
    random_numbers[i] = np.random.random()

# x is count, y is numbers
_ = plt.hist(random_numbers)

plt.show()
