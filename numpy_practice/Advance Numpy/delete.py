"""
np.delete(arr,index,axis=None) function in NumPy is used to delete elements from an array along a specified axis.
It can remove single or multiple elements based on their indices.
"""

import numpy as np

arr = np.array([10,20,30,40,50])
print("Original array:",arr)
new_arr = np.delete(arr,2) # Delete the element at index 2 (which is 30)
print("Array after deletion:",new_arr) # Output: [10 20 40 50]