import pandas as pd

# csv = "../data/imputed.csv"
csv = "../data/recoded.csv"
df = pd.read_csv(csv)
df = df.drop(columns=[df.columns[0], "patient_id"])
print("Original: ", df.shape)

df_duplicates = df[df.duplicated()]
print("Duplicates: ", df_duplicates.shape)

df_non_duplicates = df.drop_duplicates()
print("Non-Duplicates: ", df_non_duplicates.shape)

# df_non_duplicates.to_csv('../data/imputed_non_duplicates.csv', index=False)
# df_duplicates.to_csv('../data/imputed_duplicates.csv', index=False)

df_non_duplicates.to_csv('../data/recoded_non_duplicates.csv', index=False)
df_duplicates.to_csv('../data/recoded_duplicates.csv', index=False)