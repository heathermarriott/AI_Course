import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#Sample data
house_size = [1000, 1400, 2050, 2650]
house_price = [150000, 200000, 250000, 300000]

#Create a scatter plot
plt.scatter(house_size, house_price, color='blue', marker='o')
x=house_size
y=house_price
slope, intercept, r, p, std_err = stats.linregress(x, y)
print(f"slope={slope} intercept={intercept}, r={r}")

def myfunc(x):
    return slope * x + intercept

def predict(hsize, m, b):
    return m*hsize + b

sqft=int(input("Enter the house size (sqft): "))
while(sqft>0):
    print(f"prediction= ${predict(sqft, slope, intercept):,.2f}")
    sqft=int(input("Enter the house size (sqft): "))

x2=np.linspace(0, max(house_size), 5)
y2=predict(x2, slope, intercept)
plt.plot(x2, y2, 'r')

#Add labels and title
plt.title("House Prices vs. Size")
plt.xlabel("House Size (sq ft)")
plt.ylabel("House Price ($)")
plt.grid(True)

#Display the plot
plt.show()
