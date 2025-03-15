# import pandas library
import pandas as pd
import numpy as np

## Method1: Directly reading the data set from the url
## No Header in the File

# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]


file_name = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

df = pd.read_csv(file_name, header=None)

print(f'Top 10 rows of the read dataframe: {df.head(10)}')

print(f'Bottom 10 rows of the read dataframe: {df.tail(10)}')

## Adding the Headers to the Dataframe

print("headers\n", headers)

df.columns = headers
print(f'Top 10 rows of the read dataframe: ')

print(f'{df.head(10)}')