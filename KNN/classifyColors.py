#Create a graph with blue and red points
#I will use this to show how you might classify
#new points by looking at the nearby points.
#
import matplotlib.pyplot as plt
# Blue points (class 1)
x_blue = [1, 2, 3, 1, 0, 2, 3, 3]
y_blue = [4, 5, 6, 5, 3, 4, 5, 4]

# Red points (class 2)
x_red = [2, 3, 4, 3, 0, 1, 2, 4, 3]
y_red = [1, 2, 3, 1, 0, 1, 2, 1, 2]

plt.scatter(x_blue, y_blue, color='blue')
plt.scatter(x_red, y_red, color='red')

# --- Labels and legend ---
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-nearest Neighbors Example')
plt.legend()
plt.grid(True)
plt.show()
