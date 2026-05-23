﻿﻿
# This is a toy machine learning example where you classify
# a new food as a Fruit or Vegetable based on the training
# data with the 8 foods and their classification.
#
# The classification is done by using Logistic Regression
# using the sklearn.linear_model

import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegression

# --- Training data ---
X_train = [
    [7, 6],  # Apple
    [9, 2],  # Banana
    [8, 3],  # Orange
    [8, 4],  # Grape
    [3, 8],  # Carrot
    [2, 9],  # Celery
    [3, 6],  # Cucumber
    [2, 5]]  # Broccoli

y_train = [
    "Fruit", "Fruit", "Fruit", "Fruit",
    "Vegetable", "Vegetable", "Vegetable", "Vegetable"
]

# --- Plot training points ---
for (x, y), label in zip(X_train, y_train):
    color = "blue" if label == "Fruit" else "green"
    plt.scatter(x, y, color=color, s=100)

# --- Train Logistic Regression (Linear Classifier) ---
model = LogisticRegression()
model.fit(X_train, y_train)

# --- Get input for new food to classify ---
x = int(input('Enter sweetness (0-10): '))
y = int(input('Enter crunchiness (0-10): '))

# --- New food to classify ---
new_food = [[x, y]]
prediction = model.predict(new_food)[0]

print("Predicted class:", prediction)

# --- Plot new food ---
plt.scatter(x, y, color="orange", s=150, label="New food")

# --- Labels ---
plt.xlabel("Sweetness")
plt.ylabel("Crunchiness")
plt.title("Fruit vs Vegetable Classification")
plt.grid(True)

# Plot the decision boundary (a straight line for logistic regression)
x_vals = [0, 10]
y_vals = [-(model.intercept_ + model.coef_[0][0] * x) / model.coef_[0][1] for x in x_vals]
plt.plot(x_vals, y_vals, color="red", linestyle="--", label="Decision Boundary")

plt.legend()
plt.show()
