import tensorflow as tf
import matplotlib.pyplot as plt
import os

class_names = ["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
               "Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(X_train, y_train), (X_test, y_test) = fashion_mnist

# Normalize
X_train = X_train / 255.0
X_test = X_test / 255.0

model_path = "fashion_mnist_model.keras"

if os.path.exists(model_path):
    print("Loading saved model...")
    model = tf.keras.models.load_model(model_path)
else:
    print("Training new model...")
    tf.random.set_seed(43)

    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=[28,28]),
        tf.keras.layers.Dense(300, activation="relu"),
        tf.keras.layers.Dense(100, activation="relu"),
        tf.keras.layers.Dense(10, activation="softmax")
    ])

    model.compile(loss="sparse_categorical_crossentropy",
                  optimizer="sgd",
                  metrics=["accuracy"])

    history = model.fit(X_train, y_train,
                        epochs=1000,
                        validation_data=(X_test, y_test))

    model.save(model_path)
    print("Model saved.")

# ---- Load your image ----
#normally I would put the import statement at the top
#putting it here in case folks copy/paste into existing code
from tensorflow.keras.utils import load_img, img_to_array
import numpy as np 

img_path = "labCoat_28x28.png"
img = load_img(img_path, color_mode="grayscale", target_size=(28, 28))
img_array = img_to_array(img)

# Remove channel dimension (28,28,1) → (28,28)
img_array = img_array.squeeze()

# Normalize 
img_array = img_array / 255.0

# Add batch dimension
img_array = np.expand_dims(img_array, axis=0)
print("Shape going into model:", img_array.shape)

# ---- Predict ----
y_prob = model.predict(img_array)
predicted_class = np.argmax(y_prob)

print("Predicted class index:", predicted_class)
print("Predicted label:", class_names[predicted_class])

# Show image
plt.imshow(img_array[0], cmap="gray")
plt.title(f"Prediction: {class_names[predicted_class]}")
plt.axis("off")
plt.show()


