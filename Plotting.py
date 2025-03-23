# Objective of this Program
#Explore features or characteristics to predict price of car
#Analyze patterns and run descriptive statistical analysis
#Group data based on identified parameters and create pivot tables
#Identify the effect of independent attributes on price of cars
import pandas as pd
import numpy as np
import piplite
await piplite.install('seaborn')

from pyodide.http import pyfetch

async def download(url, filename):
    response = await pyfetch(url)
    if response.status == 200:
        with open(filename, "wb") as f:
            f.write(await response.bytes())

