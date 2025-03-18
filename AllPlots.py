from matplotlib import pyplot as plt

## Alternative import statement
## import matplotlib.pyplot as plt

import seaborn as sns

#Standard Line Plot

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)

plt.show()

#Scatter plot

x = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 3, 1, 2, 4, 1, 2, 3, 2, 6, 5, 4, 1, 9, 5, 2, 6, 4, 3]

plt.scatter(x, y)

plt.show()

