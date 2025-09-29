# datatype of the elements in the array

import numpy as np

arr = np.array([1, 2, 3.5, 4])
print(arr.dtype)  # Output: float64

arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr2.dtype)  # Output: <U6

arr3 = np.array([1, 2, 3], dtype=np.int8)
print(arr3.dtype)  # Output: int8

