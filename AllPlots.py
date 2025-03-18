from matplotlib import pyplot as plt

## Alternative import statement
## import matplotlib.pyplot as plt

import seaborn as sns

# Standard Line Plot

x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

plt.plot(x, y)

plt.show()

# Scatter plot

x = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
y = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 2, 3, 3, 1, 2, 4, 1, 2, 3, 2, 6, 5, 4, 1, 9, 5, 2, 6, 4, 3]

plt.scatter(x, y)

plt.show()

# Histogram
#x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
x = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]
bins = [1, 2, 3, 5, 6, 7, 9, 10, 11, 13, 14, 15, 17, 18, 19, 21, 22, 23, 25, 26, 27, 29, 30, 31, 33, 34, 35, 37, 38, 39]

#bins = [[1, 2, 3, 5, 6], [11, 13, 14, 15, 17], [19, 21, 22, 23, 25], [27, 29, 30, 31, 33], [34, 35, 37, 38, 39]]
plt.hist(x, bins, edgecolor = 'black')
plt.show()

# Bar Plot

x = ['Dell', 'HP', 'Acer', 'Compaq']
height = [70, 60, 30, 31]

plt.bar(x, height)

plt.show()

# Psuedo color plot

C = [(1, 2), (3, 5), (6, 7), (9, 10), (11, 13)]

plt.pcolor(C)

plt.show()


