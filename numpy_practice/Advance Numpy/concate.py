"""
np.concatenate((arr1,arr2),axis=0) function is used to join two or more arrays of the same shape along a specified axis.

axis=0> means the arrays will be joined along the rows (vertically).
axis=1> means the arrays will be joined along the columns (horizontally).
"""

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])

new_arr= np.concatenate((arr1,arr2))
print(new_arr) # Output: [1 2 3 4 5 6]

