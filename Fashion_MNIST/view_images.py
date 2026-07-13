#View the individual images from the MNIST Fashion dataset
#the images are 28x28 black background with which image.
# there are 10 classes of clothing.
import tensorflow as tf
import matplotlib.pyplot as plt

class_names=["T-shirt/top", "Trouser", "Pullover", "Dress", "Coat",
"Sandal", "Shirt", "Sneaker", "Bag", "Ankle Boot"]

fashion_mnist = tf.keras.datasets.fashion_mnist.load_data()
(X_train_full,y_train_full),(X_test,y_test) = fashion_mnist
item_num=0

#print(X_train_full[item_num])
print(class_names[y_train_full[item_num]])
plt.imshow(X_train_full[item_num])
plt.show() 
