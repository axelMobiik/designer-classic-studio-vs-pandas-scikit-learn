#
# Clean Missing Data
#

import pandas as pd
df = pd.read_csv('Loan+Data.csv')

# Find out the missing values
df_null = df.isnull()
df_null2 = df.isnull().sum()

# Replacing/removing the rows with missing values
df_cleanRow = df.dropna()
df_cleanColumn = df.dropna(axis=1)
