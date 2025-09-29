#ndim:- number of dimensions of the array 

import numpy as np

# arr = np.array([[1,2,3],
#                [4,5,6]])

arr = np.array([[[1,2,3],
               [4,5,6],
               [0,1,2]]])
# print(arr.ndim)# Output: 2 (2D array)

print(arr.ndim)# Output: 3 (3D array)

