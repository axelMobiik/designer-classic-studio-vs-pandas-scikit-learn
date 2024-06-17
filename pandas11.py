#
# Perform logistic regression on the defaults.csv dataset
#

import pandas as pd

# Load the data from the local files
df = pd.read_csv('defaults.csv')

# Select relevant columns from the dataset
dataPrep = df.drop(['ID'], axis=1)

# Check the missing values
dataNull = dataPrep.isnull().sum()

# Replace the missing values of string variable with mode
mode = dataPrep.mode().iloc[0]
cols = dataPrep.select_dtypes(include='object').columns

dataPrep[cols] = dataPrep[cols].fillna(mode)

# Replace numerical columns with mean
mean = dataPrep.mean()
dataPrep = dataPrep.fillna(mean)

# Create dummy variables - Not required in designet
dataPrep = pd.get_dummies(dataPrep, drop_first=True)

# Normalize the data
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
columns = df.select_dtypes(include='number').columns
dataPrep[columns] = scaler.fit_transform(dataPrep[columns])

# Create X and y - Similar to "edit columns" in Train Model
X = dataPrep.drop(['Default Next Month_Yes'], axis=1)
y = dataPrep[['Default Next Month_Yes']]

# Split Data - X and y dataset are training and testing
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=1234,
    stratify=y)

from sklearn.linear_model import LogisticRegression
lr = LogisticRegression()

# Train the model using X and y Training data
lr.fit(X_train, y_train)

# Predict the test data
y_predict = lr.predict(X_test)

# Get scored probabilities
y_prob = lr.predict_proba(X_test)[:, 1]

# Get the accuracy and confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_predict)

score = lr.score(X_test, y_test)




























