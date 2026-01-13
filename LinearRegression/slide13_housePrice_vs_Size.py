import matplotlib.pyplot as plt
import numpy as np

def initialWeightVector():
    return [0,0]  # y=0x + 0

# w has [slope, y-intercept]
def predict(X, w):
    return np.array(X) * w[0] + w[1]

def trainingLoss(X, Y, w):
    #print("training loss: ", (predict(X, w) - Y) ** 2)
    return np.average( (predict(X, w) - Y) ** 2)

def train(X, Y, w):
    #small lr, tiny steps, slower and safer
    #higher lr, faster but might overshoot best solution
    lr=.001 #learning rate(step size)
    iterations=10000
    for i in range(iterations):
       current_loss=trainingLoss(X, Y, w)
       updated_loss=trainingLoss(X, Y, [w[0]+lr, w[1]])
       updated_loss2=trainingLoss(X, Y, [w[0]-lr, w[1]])
       updated_loss3=trainingLoss(X, Y, [w[0], w[1]+lr])
       updated_loss4=trainingLoss(X, Y, [w[0], w[1]-lr])
       if updated_loss < current_loss:
            w[0] += lr
       elif updated_loss2 < current_loss:    
            w[0] -= lr
       elif updated_loss3 < current_loss:    
            w[1] += lr
       elif updated_loss4 < current_loss:    
            w[1] -= lr
       if i%100 == 0:
           loss = np.average((predict(X, w) - Y) ** 2)
           print(f" epoch {i+1} training loss: {loss:.3f}")
    print("new w = ", w)
    return w
    
# Sample data
house_size = [1000, 1400, 2050, 2650]
price = [150000, 200000, 250000, 300000]

# Create a scatter plot
plt.scatter(house_size, price, color='blue', marker='o', label='Data points')

# Draw initial line: y = 0 (slope = 0, intercept = 0)
w=initialWeightVector()
trainingLoss(house_size, price, w)
w=train(house_size, price, w)


x_vals=[0, max(house_size)]
y_vals=predict(x_vals, w)

plt.plot(
    x_vals,
    y_vals,
    color='red',
    linestyle='--',
    label='Updated line'
)

# Add labels and title
plt.title("House Prices vs. Size")
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($)")
plt.grid(True)
plt.legend()

# Display the plot
plt.show()

