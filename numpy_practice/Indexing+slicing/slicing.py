"""
slicing
 
array[start:stop:step]

array[start:stop]  # step defaults to 1

start to end -1

negative step -1

"""

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr[1:5])  # [2 3 4 5]
print(arr[1:5:2])  # [2 4]
print(arr[::2])  # [1 3 5 7 9]
print(arr[::-1])  # [9 8 7 6 5 4 3 2 1]
print(arr[-1:-5:-1])  # [9 8 7 6]
print(arr[-5:-1])  # [5 6 7 8]