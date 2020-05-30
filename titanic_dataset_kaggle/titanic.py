import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('train.csv')

print(df.shape)

print(df.head(10))

print(df.count())

plt.subplot(3, 3, 1)
plt.title('Survived')
df.Survived.value_counts(normalize=True).plot(kind='bar', alpha=0.5)

# relation between age and survival.
plt.subplot(3, 3, 2)
plt.title('Relation between survival and age')
plt.scatter(df.Pclass, df.Age, alpha=0.1)

plt.subplot(3, 3, 3)
plt.title('Survived')
df.Pclass.value_counts(normalize=True).plot(kind='bar', alpha=0.5)

plt.subplot(3, 3, 4)
plt.title('Class vs Age')
for x in [1, 2, 3]:
    df.Age[df.Pclass == x].plot(kind="kde")
plt.legend(["1st", "2nd", "3rd"])

plt.subplot(3, 3, 5)
plt.title('Embarked')
df.Embarked.value_counts(normalize=True).plot(kind="bar", alpha=0.5)

plt.subplot(3, 3, 6)
plt.title('Rich men survived')
df.Survived[(df.Sex == 'male') & (df.Pclass == 1)].value_counts(
    normalize=True).plot(kind="bar", alpha=0.5)

plt.subplot(3, 3, 7)
plt.title('Poor men survived')
df.Survived[(df.Sex == 'male') & (df.Pclass == 3)].value_counts(
    normalize=True).plot(kind="bar", alpha=0.5)


plt.tight_layout()
plt.show()
