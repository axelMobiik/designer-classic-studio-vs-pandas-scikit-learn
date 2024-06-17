# 
# Add columns and rows using Pandas
# 

import pandas as pd

dfC1 = pd.read_csv('Employee Dataset - AC1.csv')
dfC2 = pd.read_csv('Employee Dataset - AC2.csv')

# Add columns
df_ac = dfC1.join(dfC2)


dfR1 = pd.read_csv('Employee Dataset - AR1.csv')
dfR2 = pd.read_csv('Employee Dataset - AR2.csv')

# Add rows
df_arr = pd.concat([dfR1, dfR2], ignore_index=True)
