#let the user enter the x and y for a new point
#position the point on the graph with other blue and 
#red points.  our problem to solve will be 
#classifying this new point

import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier


# Blue points (class 1)
x_blue = [1, 2, 3, 1, 0, 2, 3, 3]
y_blue = [4, 5, 6, 5, 3, 4, 5, 4]

# Red points (class 2)
x_red = [2, 3, 4, 3, 0, 1, 2, 4, 3]
y_red = [1, 2, 3, 1, 0, 1, 2, 1, 2]

plt.scatter(x_blue, y_blue, color='blue')
plt.scatter(x_red, y_red, color='red')

x=int(input('Enter x value: '))
y=int(input('Enter y value: '))

plt.scatter(x, y, color='yellow')

# --- Labels and legend ---
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-nearest Neighbors Example')
plt.grid(True)
plt.show()
