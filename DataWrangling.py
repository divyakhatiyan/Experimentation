import pandas as pd
import matplotlib.pylab as plt
import numpy as np


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df = pd.read_csv(url, names = headers)

# replace "?" to NaN
df.replace("?", np.nan, inplace = True)
df.head(5)
print(df.head())

missing_data = df.isnull()
print(missing_data.head(200))

for column in missing_data.columns.values.tolist():
    print(column)
    print (missing_data[column].value_counts())
    print("")
## Replacing with Mean

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)


avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)

df["bore"].replace(np.nan, avg_bore, inplace=True)

#print(df["stroke"])

avg_stroke = df['stroke'].astype('float').mean(axis=0)

df['stroke'].replace(np.nan, avg_stroke, inplace=True)

print(df["horsepower"])

avg_hpower = df['horsepower'].astype('float').mean(axis=0)

df['horsepower'].replace(np.nan, avg_hpower, inplace=True)

#Conversion to correct data types
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")