import tensorflow as tf
import matplotlib.pyplot as plt

class_names=["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
"Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
print(len(fashion_mnist), type(fashion_mnist))
(X_train_full,y_train_full),(X_test,y_test) = fashion_mnist

# Normalize, data is 0-255, neural networks work better 0-1
X_train = X_train_full / 255.0
X_test = X_test / 255.0

tf.random.set_seed(43) 
model = tf.keras.Sequential()
model.add(tf.keras.layers.Input(shape=[28,28])) #our images are 28x28
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(300, activation="relu"))
model.add(tf.keras.layers.Dense(100, activation="relu"))
model.add(tf.keras.layers.Dense(10, activation="softmax"))

model.summary()

model.compile(loss="sparse_categorical_crossentropy",
              optimizer="sgd",
              metrics=["accuracy"])

history = model.fit(X_train, y_train_full, epochs=60,
                    validation_data=(X_test, y_test))
