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
#### Average for normalised loss and replacement of NAN with average value

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

## Average for bore and replacement of NAN with average value

avg_bore=df['bore'].astype('float').mean(axis=0)
print("Average of bore:", avg_bore)
df["bore"].replace(np.nan, avg_bore, inplace=True)

#print(df["stroke"])

## Average for stroke and replacement of NAN with average value

avg_stroke = df['stroke'].astype('float').mean(axis=0)

df['stroke'].replace(np.nan, avg_stroke, inplace=True)

print(df["horsepower"])

## Average for Horse power and replacement of NAN with average value

avg_hpower = df['horsepower'].astype('float').mean(axis=0)
df['horsepower'].replace(np.nan, avg_hpower, inplace=True)

## Average for peak rpm and replacement of NAN with average value

avg_peakrpm=df['peak-rpm'].astype('float').mean(axis=0)
print("Average peak rpm:", avg_peakrpm)
df['peak-rpm'].replace(np.nan, avg_peakrpm, inplace=True)

print(f'Number of door: {df["num-of-doors"].value_counts()}')

#We can also use the ".idxmax()" method to calculate the most common type automatically:

print(f'Maximum Number of door:{df["num-of-doors"].value_counts().idxmax()}')
#replace the missing 'num-of-doors' values by the most frequent
df["num-of-doors"].replace(np.nan, "four", inplace=True)

# simply drop whole row with NaN in "price" column
df.dropna(subset=["price"], axis=0, inplace=True)

# reset index, because we droped two rows
df.reset_index(drop=True, inplace=True)

df.dtypes


df.head()

# Convert mpg to L/100km by mathematical operation (235 divided by mpg)
df['city-L/100km'] = 235/df["city-mpg"]

# check your transformed data
df.head()

#Conversion to correct data types
df[["bore", "stroke"]] = df[["bore", "stroke"]].astype("float")
df[["normalized-losses"]] = df[["normalized-losses"]].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")