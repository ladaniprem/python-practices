"""
np.insert() function in NumPy is used to insert values into an array at specified indices. 
It allows you to add elements along a specified axis without modifying the original array. 
The function takes three main arguments: the original array, the index or indices where the new values should be inserted, and the values to be inserted.

array - input array
index - index or indices before which values is inserted
values - values to be inserted into array
axis - axis along which to insert values. If axis is not specified, the input array is flattened before insertion.
axis=0,rows-wise insertion
axis=1,column-wise insertion
"""

import numpy as np

arr = np.array([1,2,3,4,6,7])
print("Original array:",arr)
new_arr = np.insert(arr,2,50)
print("New array after insertion:",new_arr)

