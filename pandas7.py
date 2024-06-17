#
# Data Normalization using MinMax and Standard Scalers
#

import pandas as pd

df = pd.read_csv('defaults.csv')

# MinMaxScaler - All data is normalized to a range between 0 and 1, proportional to the actual data
dataminmax = df.copy()
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()

columns = dataminmax.select_dtypes(include='number').columns
dataminmax[columns] = scaler.fit_transform(dataminmax[columns])

# Z-Score - All data is normalized to a smaller range, proportional to the actual data
datastandard = df.copy()
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

columns = datastandard.select_dtypes(include='number').columns
datastandard[columns] = scaler.fit_transform(datastandard[columns])
