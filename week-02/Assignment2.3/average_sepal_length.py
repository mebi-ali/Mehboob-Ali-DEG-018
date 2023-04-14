# Import pandas and numpy libraries
import pandas as pd
import numpy as np

# Define function to calculate average sepal length for each species
def average_sepal_length(df):
    return df.groupby('Species').agg({'SepalLengthCm': np.mean})

# Load Iris data into pandas dataframe and calculate average sepal length
df = pd.read_csv('./Iris.csv')

# Prints the result
print(average_sepal_length(df))  
