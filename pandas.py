#
# Use Pandas for data processing
#

import pandas as pd

# Get the csv using pandas
df = pd.read_csv('Loan+Data.csv')
df.head()

# Read the tab delimited data
df_tab = pd.read_csv('Loan+Data+Tab.txt', sep='\t')
df_tab.head()

# Read the data from URL
columns = ['age', 'wc', 'fw', 'edu', 'edu_num', 
           'ms', 'occ', 'rel', 'race', 'gender', 
           'cg', 'cl', 'hpw', 'nc', 'income']
df_h = pd.read_csv(
        'https://archive.ics.uci.edu/ml/machine-learning-databases/adult/adult.data',
        header=None,
        names=columns
    )
df_h.head()

# Select columns from the dataset - For random selection
df_selected = df_h[['age', 'income']]

#Select columns using iloc - For larger datasets
df_iloc = df.iloc[0:5, 1:4]

# Select columns using negative index
X = df.iloc[:, :-1] # All columns except the last one
Y = df.iloc[:, -1:] # The last column

# Drop columns from a dataframe
df_d = df.drop(['Loan_ID', 'Gender'], axis=1)
