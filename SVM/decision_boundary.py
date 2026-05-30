# Simple case of using support vector machine to classify 
# my red stars and blue dots.
#
# the support vectors (points closest to decision boundary)
# are very important in determining the equation of the decision
# boundary line
#
# in higher dimensions, the line could become a plane or hyperplane
# some ChatGPT assistance with the vertical line decision boundary
#
from sklearn import svm
import matplotlib.pyplot as plt

X = [
    # Class 0 (left side)
    [0.5, 0.5],
    [0.5, 1.5],
    [1.0, 1.0],
    [1.0, 2.5],
    [1.5, 0.5],
    [1.5, 2.0],
    [2.0, 1.0],

    # Class 1 (right side)
    [3.0, 1.0],
    [3.5, 0.5],
    [3.5, 2.0],
    [4.0, 1.0],
    [4.0, 3.0],
    [4.5, 1.5],
    [4.5, 2.5]
]

y = [
    0,0,0,0,0,0,0,
    1,1,1,1,1,1,1
]

for point, label in zip(X, y):
    if label == 0:
        plt.plot(point[0], point[1], 'r*', markersize=10)
    else:
        plt.plot(point[0], point[1], 'bo')

plt.grid(True)
plt.axis([0, 5, 0, 4])


clf = svm.SVC(kernel='linear')
clf.fit(X,y)
print("y-intercept", clf.intercept_)
print("coeficent", clf.coef_)

# decision boundary : w0 x + w1 y + b =0
x_vals=[0, 3, 6]
w0=clf.coef_[0][0]
w1=clf.coef_[0][1]
b=clf.intercept_[0]


# -----------------------------
# HANDLE VERTICAL LINE CASE
# -----------------------------
if abs(w1) < 1e-10:
    # vertical line: x = constant
    x_line = -b / w0
    plt.axvline(x_line, color='k', label='decision boundary')
else:
    x_vals = np.linspace(0, 5, 100)
    y_vals = -(w0 * x_vals + b) / w1
    plt.plot(x_vals, y_vals, 'k-', label='decision boundary')

plt.legend()
plt.show()
