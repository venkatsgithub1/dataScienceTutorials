import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# normal distribution with mu = 20, std = 1 and 10000 samples
samples_std1 = np.random.normal(20, 1, size=10000)
# increasing deviation
samples_std2 = np.random.normal(20, 3, size=10000)
samples_std3 = np.random.normal(20, 10, size=10000)

sns.set()

_ = plt.hist(samples_std1, histtype='step', density=True, bins=100)
_ = plt.hist(samples_std2, histtype='step', density=True, bins=100)
_ = plt.hist(samples_std3, histtype='step', density=True, bins=100)

_ = plt.legend(('std = 1', 'std = 3', 'std = 10'))
plt.ylim(-0.01, 0.42)
plt.show()
