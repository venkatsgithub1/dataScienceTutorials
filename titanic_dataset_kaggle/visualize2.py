import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')

print(df.shape)

print(df.head(10))

print(df.count())

plt.subplot(2, 3, 1)
plt.title('Survived')
df.Survived.value_counts(normalize=True).plot(kind='bar', alpha=0.5)

plt.subplot(2, 3, 2)
plt.title('Men Survived')
df.Survived[df.Sex == "male"].value_counts(
    normalize=True).plot(kind='bar', alpha=0.3)

plt.subplot(2, 3, 3)
plt.title('Women Survived')
df.Survived[df.Sex == "female"].value_counts(
    normalize=True).plot(kind='bar', alpha=0.3)

plt.subplot(2, 3, 4)
plt.title('Sex Survived')
df.Sex[df.Survived == 1].value_counts(
    normalize=True).plot(kind="bar", alpha=0.5)

plt.show()
