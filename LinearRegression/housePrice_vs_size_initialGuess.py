import matplotlib.pyplot as plt
import numpy as np

def initialWeightVector():
    return [0,0]  # y=0x + 0

# w has [slope, y-intercept]
def predict(X, w):
    return np.array(X) * w[0] + w[1]

def trainingLoss(X, Y, w):
    print("training loss: ", (predict(X, w) - Y) ** 2)
    return np.average( (predict(X, w) - Y) ** 2)
    

# Sample data
house_size = [1000, 1400, 2050, 2650]
price = [150000, 200000, 250000, 300000]

# Create a scatter plot
plt.scatter(house_size, price, color='blue', marker='o', label='Data points')

# Draw initial line: y = 0 (slope = 0, intercept = 0)
w=initialWeightVector()
trainingLoss(house_size, price, w)

plt.plot(
    [0, max(house_size)],
    [w[0], w[1]],
    color='red',
    linestyle='--',
    label='Initial line (slope=0)'
)

# Add labels and title
plt.title("House Prices vs. Size")
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($)")
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
