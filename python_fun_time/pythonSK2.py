import numpy as np
from sklearn import tree

#data
from sklearn.datasets import load_iris
iris = load_iris()

#train data
test_idx_[0,50,100]
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

#test data
test_target = iris.target

clf = tree.DecitionTreeClassifier
clf.fit(train_data, train_target)

print test_target