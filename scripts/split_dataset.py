import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# csv = "../data/non_duplicates.csv"
csv = "../data/recoded_non_duplicates.csv"
df = pd.read_csv(csv)

train, test = train_test_split(df, test_size=0.2, random_state=42)

print("Original: ", df.shape)
print("Train: ", train.shape)
print("Test: ", test.shape)

# train.to_csv('../data/train.csv', index=False)
# test.to_csv('../data/test.csv', index=False)

train.to_csv('../data/recoded_train.csv', index=False)
test.to_csv('../data/recoded_test.csv', index=False)
