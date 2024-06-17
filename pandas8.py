#
# Label Encoding of the categorical columns using pandas - Convert the categorical values to 0, 1...
# 

import pandas as pd

df = pd.read_csv('defaults.csv')
df = df.drop(['ID'], axis=1)

# Get the column names of the object/string type of columns
columns = df.select_dtypes(include='object').columns

# Change the object datatype to category
df[columns] = df[columns].astype('category')

# Check the datatype
df.dtypes

# Create a copy of df
dt = df.copy()

# Drop missing values
dt = dt.dropna()

# cat.codes for label encoding applied on series
for column in columns:
    dt[column] = dt[column].cat.codes
    