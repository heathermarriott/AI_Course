# updated example where one of the support vectors is moved
# this decision boundary is not vertical, so we don't 
# need an if for that case
#
from sklearn import svm
import matplotlib.pyplot as plt
import numpy as np

# -------------------------
# DATA
# -------------------------
X = [
    [0.5, 5],[0.5, 4],[1.0, 4],[1.0, 5],
    [1, 3.5],[1.5, 4.5],
    [2.0, 1.0],
    [8.0, 1.0], #changed one of the support vectors
    [5.5, 0.5],[6.5, 2.0],
    [7.3, 1.0],[6.2, 3.0],[5.8, 1.5],[5.9, 2.5]
]

y = [0]*7 + [1]*7

# -------------------------
# PLOT POINTS
# -------------------------
for p, label in zip(X, y):
    if label == 0:
        plt.plot(p[0], p[1], 'r*', markersize=10)
    else:
        plt.plot(p[0], p[1], 'bo')

# -------------------------
# TRAIN LINEAR SVM
# -------------------------
clf = svm.SVC(kernel='linear', C=1e6)
clf.fit(X, y)

w = clf.coef_[0]
b = clf.intercept_[0]

print("w:", w)
print("b:", b)

# -------------------------
# PLOT SUPPORT VECTORS
# -------------------------
plt.scatter(
    clf.support_vectors_[:, 0],
    clf.support_vectors_[:, 1],
    s=150,
    facecolors='none',
    edgecolors='k',
    label="support vectors"
)

X_np = np.array(X)

x_vals = np.linspace(X_np[:,0].min() - 1,
                     X_np[:,0].max() + 1,
                     400)

w = clf.coef_[0]
b = clf.intercept_[0]

y_decision = -(w[0]*x_vals + b) / w[1]
y_margin_up = -(w[0]*x_vals + b - 1) / w[1]
y_margin_down = -(w[0]*x_vals + b + 1) / w[1]

plt.plot(x_vals, y_decision, 'k-', label="decision boundary")
plt.plot(x_vals, y_margin_up, 'k--')
plt.plot(x_vals, y_margin_down, 'k--')

x_vals = np.linspace(X_np[:,0].min() - 1,
                     X_np[:,0].max() + 1,
                     400)
# -------------------------
# FINAL SETTINGS
# -------------------------
plt.xlim(0, 9)
plt.ylim(0, 8)
plt.grid(True)
plt.legend()
plt.show()
