# %%
# Imports
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.metrics import f1_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Import the Wine dataset from scikit-learn
wine = datasets.load_wine()

# Extract the features and target variable from the dataset
Wine_Data_x = wine.data[:, 2:]
Wine_Data_y = wine.target


# Load the Wine dataset and separate it into training and testing sets
Wine_Data = datasets.load_wine()
x_train, x_test, y_train, y_test = train_test_split(Wine_Data_x, Wine_Data_y, test_size=0.2)

# Scale the training and testing features using the StandardScaler class
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# Create a logistic regression model using the LogisticRegression class and fit it on the training data
model = LogisticRegression()
model.fit(x_train, y_train)

# Use the model to predict the target variable for the testing data
y_pred = model.predict(x_test)

# Calculate the f1-score to evaluate the accuracy of the model
print(f1_score(y_test, y_pred, average="micro"))



