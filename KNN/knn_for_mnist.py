#This program uses the K-Nearest Neighbors
#algorithm to classify the MNIST dataset
#The K is 3 in this case.  We look at the
#3 closest neighbors to help us classify 
#the images.
#
#KNN is a simple to understand algorithm and
#gives a pretty good accuracy. ~97%
#we can get even better accuracy with a
#neural network, but that code will become more 
#complex.

from tensorflow.keras.datasets import mnist
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(f"# Training Images: {len(X_train)} ")
print(f"# Testing Images: {len(X_test)}")

# Reshape the images from 28x28 to a 784-element vector
X_train_reshaped = X_train.reshape(len(X_train), -1)
X_test_reshaped = X_test.reshape(len(X_test), -1)

# --- Create and train kNN classifier ---
# look at the 3 closest neighbors when deciding classification
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train_reshaped, y_train)

# --- Predict on test set ---
y_pred = knn.predict(X_test_reshaped)

# --- Calculate accuracy ---
accuracy = (y_pred == y_test).mean()
print("Test accuracy:", accuracy)

# --- Optional: check one prediction ---
n = 0
print(f"True label: {y_test[n]}, Predicted: {y_pred[n]}")
plt.imshow(X_test[n])
plt.show()
