#
# Change the data type of a column
#

import pandas as pd

df = pd.read_csv('Loan+Data.csv')

# Get the data types
df.dtypes

# Change credit history to categorical
df['Credit_Hisroty'] = df['Credit_History'].astype('category')
df.dtypes

# Summarise the data
df.describe()
df_summary = df.describe(include='all', percentiles=[0.01, 0.05, 0.1, 0.9, 0.99, 0.995])
