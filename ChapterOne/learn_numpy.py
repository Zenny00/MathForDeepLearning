import numpy as np

print(np.__version__)

a = np.array([1,2,3,4])

print("Array: {}".format(a))
print("Size: {}".format(a.size))
print("Shape: {}".format(a.shape))
print("Data Type: {}".format(a.dtype))

# Array of arrays
b = np.array([[1,2,3,4],[5,6,7,8]])
print(b)
print(b.shape)
