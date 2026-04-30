import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier

# Blue points (class 1)
x_blue = [1, 2, 3, 1]
y_blue = [4, 5, 6, 5]

# Red points (class 2)
x_red = [0.5, 1.5, 2.5]
y_red = [6, 8, 9]

# Combine data
points = list(zip(x_blue, y_blue)) + list(zip(x_red, y_red))
labels = ['blue'] * len(x_blue) + ['red'] * len(x_red)

# New point
new_point = [[0.9, 5.8]]  # must be 2D for sklearn

# --- KNN with scikit-learn ---
k = 3
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(points, labels)

predicted_class = knn.predict(new_point)[0]

print(f"Predicted class for {new_point[0]}: {predicted_class}")

# Plot original points
plt.scatter(x_blue, y_blue, color='blue', label='Class Blue')
plt.scatter(x_red, y_red, color='red', label='Class Red')

# Plot new point (colored by prediction)
plt.scatter(new_point[0][0], new_point[0][1], color='y', label='New Point')

# Labels and legend
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.title('K-nearest Neighbors Example (sklearn)')
plt.legend()
plt.grid(True)

plt.show()

