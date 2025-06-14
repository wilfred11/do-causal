import pandas as pd
import numpy as np

from data import read_data
from agrum import learn

data, age_labels =read_data()
print(data.head)
print(data.columns)
#print(data['Age-group'])
#print(data['Education_Level'].unique())
#print(data['Salary'].unique())

#print(data['Salary'].min())


#print(data['Salary'].unique())
print(data['Salary'].unique().min())
print(data['Salary'].unique().max(), data['Salary'].unique().max(), 10)

salary_values = list(range(int(data['Salary'].unique().min()), int(data['Salary'].unique().max())+10, 10))
exp_values = list(range(int(data['XP'].unique().min()), int(data['XP'].unique().max())+1, 1))
print(exp_values)

learn(data, age_labels,salary_values, exp_values)



