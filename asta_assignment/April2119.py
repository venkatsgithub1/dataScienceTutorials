import pandas as pd
import statsmodels.api as sm
from statsmodels.formula.api import ols
import matplotlib.pyplot as plt

df = pd.read_csv('2)BlueGills.csv')

mod=ols('length ~ age', data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

grps = pd.unique(df['age'].values)

print(grps)

d_data = {grp: df['length'][df.age == grp] for grp in grps}

from scipy import stats

f, p = stats.f_oneway(d_data[1], d_data[2], d_data[3], d_data[4], d_data[5], d_data[6])

print(f, p)