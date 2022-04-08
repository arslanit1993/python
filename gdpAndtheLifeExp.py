
#Find the mean and the mode of the life expectancy and the gdp per capita 

import numpy as np
import pandas as pd
import seaborn as sns
import gapminder as gapminder
import statistics as sts
import matplotlib.pyplot as plt



df = pd.read_csv('gapminder.csv')

#Mean and the mode of the gdp per capita 
meanGdp = np.mean(df['gdp_per_capita'])
modeGdp = sts.mode(df['gdp_per_capita'])

#Mean nad the mode for the life expectancy
meanLifeExp = np.mean(df['life_expectancy'])
modeLifeExp = sts.mode(df['life_expectancy'])


print('mean for the GDP = ', meanGdp)
print('mode of the GDP  = ', modeGdp)

print('mean for the life expectancy = ', meanLifeExp)
print('mode of the life Expectancy = ', modeLifeExp)

#Histogram for the gdp per capita 
sns.distplot(df['gdp_per_capita'])
