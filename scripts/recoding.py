import pandas as pd

csv = "../data/test_with_clusters.csv"
df = pd.read_csv(csv)
# df = df.drop(columns=[df.columns[0], "patient_id"])

df['gender'] = df['gender'].map({'M': 'Male', 'F': 'Female'})
df['has_hypertension'] = df['has_hypertension'].map({0 : 'No', 1 : 'Yes'})
df['has_heart_disease'] = df['has_heart_disease'].map({0 : 'No', 1 : 'Yes'})
df['marital_status'] = df['marital_status'].map({0 : 'No', 1 : 'Yes'})
df['high_glucose'] = df['high_glucose'].map({0 : 'No', 1 : 'Yes'})
df['stroke_event'] = df['stroke_event'].map({0 : 'No', 1 : 'Yes'})

df.to_csv('../data/recoded_test.csv', index=False)
