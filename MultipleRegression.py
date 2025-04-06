'''
Dependencies
!pip install numpy==2.2.0
!pip install pandas==2.2.3
!pip install scikit-learn==1.6.0
!pip install matplotlib==3.9.3
'''
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"

'''
Understand the data

    MODEL YEAR e.g. 2014
    MAKE e.g. VOLVO
    MODEL e.g. S60 AWD
    VEHICLE CLASS e.g. COMPACT
    ENGINE SIZE e.g. 3.0
    CYLINDERS e.g 6
    TRANSMISSION e.g. AS6
    FUEL TYPE e.g. Z
    FUEL CONSUMPTION in CITY(L/100 km) e.g. 13.2
    FUEL CONSUMPTION in HWY (L/100 km) e.g. 9.5
    FUEL CONSUMPTION COMBINED (L/100 km) e.g. 11.5
    FUEL CONSUMPTION COMBINED MPG (MPG) e.g. 25
    CO2 EMISSIONS (g/km) e.g. 182

Your task will be to create a multiple linear regression model using some of these features to predict CO2 emissions of unobserved cars based on the selected features. 
'''

'''
Load the data
'''
df = pd.read_csv(url)

# verify successful load with some randomly selected records
print(df.sample(5))
"Explore and select features"
print(df.describe())

# Drop categoricals and any unseless columns
df = df.drop(['MODELYEAR', 'MAKE', 'MODEL', 'VEHICLECLASS', 'TRANSMISSION', 'FUELTYPE',],axis=1)

df.corr()

'''
Look at the bottom row, which shows the correlation between each variable and the target, 'CO2EMISSIONS'. Each of these shows a fairly high level of correlation, each exceeding 85% in magnitude. Thus all of these features are good candidates.

Next, examine the correlations of the distinct pairs. 'ENGINESIZE' and 'CYLINDERS' are highly correlated, but 'ENGINESIZE' is more correlated with the target, so we can drop 'CYLINDERS'.

Similarly, each of the four fuel economy variables is highly correlated with each other. Since FUELCONSUMPTION_COMB_MPG is the most correlated with the target, you can drop the others: 'FUELCONSUMPTION_CITY,' 'FUELCONSUMPTION_HWY,' 'FUELCONSUMPTION_COMB.'

Notice that FUELCONSUMPTION_COMB and FUELCONSUMPTION_COMB_MPG are not perfectly correlated. They should be, though, because they measure the same property in different units. In practice, you would investigate why this is the case. You might find out that some or all of the data is not useable as is.

'''
df = df.drop(['CYLINDERS', 'FUELCONSUMPTION_CITY', 'FUELCONSUMPTION_HWY','FUELCONSUMPTION_COMB',],axis=1)