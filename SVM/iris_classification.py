# Iris Classification is a Hello World problem in
# machine learning.  
#
# Allow the user to type in sepal and petal
# length and with in cm and print the classification
#
from sklearn import svm, datasets

iris=datasets.load_iris()
X = iris.data
y = iris.target
clf = svm.SVC()
clf.fit(X,y)

s_l=float(input('Enter the sepal length: '))
s_w=float(input('Enter the sepal width: '))
p_l=float(input('Enter the petal length: '))
p_w=float(input('Enter the petal width: '))
p = clf.predict([[s_l, s_w, p_l, p_w]])
print(p)
if p==0:
    print("Iris Setosa")
elif p==1:
    print("Iris Versicolor")
else:
    print("Iris Virginica")
