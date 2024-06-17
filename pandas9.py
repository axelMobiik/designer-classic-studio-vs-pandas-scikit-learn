#
# Hot Encoding of the categorical columns
# Best way to categorize data and convert it into numeric
# For example: instead of assigning type values
# London: 1; New York: 2; England: 3
# The London, New York and England columns will be created 
# and will have a value of 1 if true and 0 if not.
#

import pandas as pd

df = pd.read_csv('defaults.csv')
df = pd.drop(['ID'], axis=1)

# CReate dummy variables from categorical or object columns
df_dummy = pd.get_dummies(df)
