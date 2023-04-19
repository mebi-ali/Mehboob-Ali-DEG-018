
import numpy as np
import pandas as pd

# Load Data
df = pd.read_csv('./Data/cars.csv')

# Sample of Data
df.sample(10)


def label_encoder(row):
    # get unique values in the row
    values = row.unique()
    # create empty dictionary to store labels
    labels = {}
    # loop through unique values and assign a label
    for key, values in enumerate(values):
        labels[values] = key        
    # create a new Pandas series with labels for each value
    return pd.Series([ labels[value] for value in labels] )

# select columns of object type and apply label_encoder function to each row
# print first 5 rows of the resulting dataframe
df.select_dtypes('object').apply(label_encoder).head()




