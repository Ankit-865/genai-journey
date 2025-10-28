#as type 
import numpy as np
arr = np.array([1.5, 2.3, 3.7])
print(arr.dtype)
new_arr = arr.astype(int)

print(new_arr.dtype)