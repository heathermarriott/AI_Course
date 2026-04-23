from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt

(X_train, y_train), (X_test, y_test) = mnist.load_data()
print(len(X_train))
print(len(X_test))
print(len(y_train))
print(len(y_test))

plt.imshow(X_train[0])
plt.show()
print(y_train[0])
