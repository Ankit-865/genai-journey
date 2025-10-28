import numpy as np
arr = np.array([[1, 2], [4, 5]])
print (arr)
new_arr = np.insert(arr, 1, [99, 12], axis=None)
print (new_arr)