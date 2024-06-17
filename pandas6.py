#
# Write the dataframe to a csv or a delimited file
#

import pandas as pd

df = pd.read_csv('Loan+Data.csv')
df_tab = pd.read_csv('Loan+Data+Tab.txt')

# Replacing/removing the rows with missing values
df_clean = df.dropna()
df_tab_clean = df.dropna()

# Save a csv file
df_clean.to_csv('./data/Clean Loan data.csv', index=False)

# Tab limited
df_tab_clean.to_csv('./data/Clean Loan data Tab.txt', index=False, sep='\t')
