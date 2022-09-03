# importing Python library
import numpy as np

# define Unit Step Function
def unitStep(v):
	if v >= 0:
		return 1
	else:
		return 0

# design Perceptron Model
def perceptronModel(x, w, b):
	v = np.dot(w, x) + b
	y = unitStep(v)
	return y

# AND Logic Function
# w1 = 1, w2 = 1, b = -1.5
def LogicFunction(x):
	w = np.array([1, 1])
	b = -1.5
	return perceptronModel(x, w, b)

# testing the Perceptron Model
test1 = np.array([0, 1])
test2 = np.array([1, 1])
test3 = np.array([0, 0])
test4 = np.array([1, 0])


print(f"AND {0}, {1} = {LogicFunction(test1)} ")
print(f"AND {1}, {1} = {LogicFunction(test2)}")
print(f"AND {0}, {0} = {LogicFunction(test3)}")
print(f"AND {1}, {0} = {LogicFunction(test4)}")