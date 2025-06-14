import pandas as pd
import numpy as np

def read_data():
    df = pd.read_csv('./data/Salary_Data.csv')
    print(df.info())

    df.rename(columns=lambda x: x.replace(' ', '_'), inplace=True)

    numeric = ['Age', 'Years_of_Experience', 'Salary']
    for col in numeric:
        df[col].fillna(df[col].mean(), inplace=True)

    categorical = ['Gender', 'Education_Level']
    for col in categorical:
        mode_val = df[col].mode()[0]
        df[col].fillna(mode_val, inplace=True)

    df['Education_Level'] = np.where(df['Education_Level'] == "PhD", 1, 0)

    bins = [18, 30, 40, 50, 60, 70, 120]
    age_labels = ['18-29', '30-39', '40-49', '50-59', '60-69', '70+']
    df['Age-group'] = pd.cut(df.Age, bins, labels=age_labels, include_lowest=True)

    df = df[['Age-group',
             'Gender',
             'Education_Level',
             'Years_of_Experience',
             'Salary']]

    df['Salary']= (np.ceil(df.Salary/10))*10

    print(df["Salary"])

    df.rename(columns={'Years_of_Experience': 'XP', 'Education_Level': 'PhD'}, inplace=True)

    #df['Salary']=df['Salary']

    convert_dict = {'Salary': int, 'XP':int}

    df = df.astype(convert_dict)

    return df, age_labels
