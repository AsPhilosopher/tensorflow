import numpy as np

data1 = np.array([1, 2, 3, 4, 5])
data2 = np.array([[1, 2], [3, 4]])
print(data1)
print(data2)
print(data1.shape, data2.shape)
print(np.zeros([2, 3]), np.ones([3, 2]))
data2[1, 0] = 5
print(data2)
print(data2[1, 1])

data3 = np.ones([2, 3])
print(data3 * 3)
print(data3 / 3)
print(data3 + 2)

data4 = np.array([[1, 2, 3], [4, 5, 6]])
print(data3 + data4)
print(data3 * data4)
