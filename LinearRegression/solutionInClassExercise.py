import matplotlib.pyplot as plt
import numpy as np

# Sample data
temp_f = [ 40, 55, 92, 87]
num_customers=[ 2, 5, 20, 17]

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
       updated_loss=trainingLoss(X, Y,[w[0]+lr, w[1]])
       #print(f"try updating slope to: {w[0]+lr} => loss {updated_loss}")
       updated_loss2=trainingLoss(X, Y, [w[0]-lr, w[1]])
       #print(f"try updating slope to: {w[0]-lr} => loss {updated_loss2}")
       updated_loss3=trainingLoss(X, Y, [w[0], w[1]+lr])
       #print(f"try updating y-intercept to: {w[1]+lr} => loss {updated_loss3}")
       updated_loss4=trainingLoss(X, Y, [w[0], w[1]-lr])
       #print(f"try updating y-intercept to: {w[0]+lr} => loss {updated_loss4}")
       #print(f"current_loss={current_loss} ****");
       
       #x=input("")
       if updated_loss < current_loss:
            w[0] += lr
            #print("  update 1")
       elif updated_loss2 < current_loss:    
            w[0] -= lr
            #print("  update 2")
       elif updated_loss3 < current_loss:    
            w[1] += lr
            #print("  update 3")
       elif updated_loss4 < current_loss:    
            w[1] -= lr
            #print("  update 4")
       else:
           print("None of updates improve the model.")
           break
       if i%100 == 0:
           loss = np.average((predict(X, w) - Y) ** 2)
           print(f" epoch {i+1} training loss: {loss:.3f}")
    print("new w = ", w)
    return w
    

# Create a scatter plot
plt.scatter(temp_f, num_customers, color='blue', marker='o', label='Data points')

# Draw initial line: y = 0 (slope = 0, intercept = 0)
w=initialWeightVector()
w=train(temp_f, num_customers, w)


x_vals=[0, max(temp_f)]
y_vals=predict(x_vals, w)

plt.plot(
    x_vals,
    y_vals,
    color='red',
    linestyle='--',
    label='Updated line'
)

# Add labels and title
plt.title("Temp vs. # Customers")
plt.xlabel("Temp (F)")
plt.ylabel("# Customers")
plt.grid(True)
plt.legend()

# Display the plot
plt.show()
