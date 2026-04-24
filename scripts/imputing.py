import pandas as pd

csv = "../data/healthcare_data.csv"
df = pd.read_csv(csv)

normal_mean=22.16
obese_mean=36.28
overweight_mean=27.45
underweight_mean=16.64

for index, row in df.iterrows():  
    if pd.isna(row['bmi_value']):
        if row['bmi_category'] == 'normal':
            df.loc[index, 'bmi_value'] = normal_mean
        elif row['bmi_category'] == 'obese':
            df.loc[index, 'bmi_value'] = obese_mean
        elif row['bmi_category'] == 'overweight':
            df.loc[index, 'bmi_value'] = overweight_mean
        elif row['bmi_category'] == 'underweight':
            df.loc[index, 'bmi_value'] = underweight_mean


df.to_csv('../data/imputed.csv', index=False)