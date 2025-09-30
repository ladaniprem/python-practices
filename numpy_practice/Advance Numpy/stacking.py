"""
vertically
horizontally

vstack() row wise
hstack() column wise
"""

import numpy as np

arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr2 = np.array([[7, 8, 9], [10, 11, 12]])
print(np.vstack((arr1, arr2)))  # Vertical stacking
print(np.hstack((arr1, arr2)))  # Horizontal stacking