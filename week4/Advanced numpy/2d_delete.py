import numpy as np
arr1 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr1)
new_arr = np.delete(arr1, 1, axis=0)
print(new_arr)