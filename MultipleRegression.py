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
df.sample(5)
