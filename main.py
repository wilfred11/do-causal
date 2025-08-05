from locale import normalize

import pandas as pd

from data import BinaryDataGenerator

generator = BinaryDataGenerator(population_size=800, columns=["smoking", "tar", "cancer"], random_state=42)
generator.set_values(col_name="smoking", frac=0.5)
generator.set_values(col_name="tar", frac=0.85, condition=generator.data["smoking"]==0)
generator.set_values(col_name="tar", frac=0.65, condition=generator.data["smoking"]==1)
generator.set_values(col_name="cancer", frac=0.85, condition=((generator.data["smoking"]==1) & (generator.data["tar"]==1)))
generator.set_values(col_name="cancer", frac=0.1, condition=((generator.data["smoking"]==1) & (generator.data["tar"]==0)))
generator.set_values(col_name="cancer", frac=0.35, condition=((generator.data["smoking"]==0) & (generator.data["tar"]==1)))
generator.set_values(col_name="cancer", frac=0.15, condition=((generator.data["smoking"]==0) & (generator.data["tar"]==0)))
df_smoking = generator.data

df_summary = df_smoking.groupby(["cancer"]).value_counts().reset_index().iloc[:, [1, 2, 0, 3]]
df_summary.rename(columns={0: "count"}, inplace=True)
print(df_summary)


smoking=df_smoking.filter(items=['smoking']).value_counts(normalize=True)
smoking_tar=df_smoking.filter(items=['smoking',"tar"]).groupby("smoking").value_counts(normalize=True)
smoking_tar_cancer=df_smoking.filter(items=['smoking',"tar","cancer"]).groupby(["smoking","tar"]).value_counts(normalize=True)

print(smoking)
print(smoking_tar)
print(smoking_tar_cancer)

P_Y_doX_1=(0.65*((0.35*0.5)+(0.85*0.5)) + 0.35*((0.15*0.5)+(0.10*0.5)))
print(P_Y_doX_1)
P_Y_doX_0=(0.55*((0.35*0.5)+(0.85*0.5)) + 0.45*((0.15*0.5)+(0.10*0.5)))
print(P_Y_doX_0)
ace = P_Y_doX_1- P_Y_doX_0
print("The average effect of smoking on cancer:")
print("For every rise of 1 unit in smoking there is a "+str(ace)+" rise in cancer")








