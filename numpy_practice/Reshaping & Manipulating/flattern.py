"""
.ravel() returns a contiguous flattened array. --> view
.flatten() returns a copy of the original array collapsed into one dimension.--> copy
Both functions are used to convert a multi-dimensional array into a one-dimensional array.

ravel()
Returns a flattened view of the array if possible (i.e., no copy is made, just a new "view" of the same memory).
If a view is not possible, it falls back to returning a copy.
More memory efficient.

flatten()
Always returns a copy of the array.
Changes to the flattened array do not affect the original array.
Slightly slower because of the copy.
"""

import numpy as np

arr_2d = np.array([[1,2,3],
                   [4,5,6]])

print(arr_2d.ravel())  # Output: [1 2 3 4 5 6]
print(arr_2d.flatten())  # Output: [1 2 3 4 5 6]

#flatten
arr = np.array([[1, 2], [3, 4]])
f = arr.flatten()
f[0] = 100
print(arr)   # arr does NOT change

#ravel
import numpy as np
arr = np.array([[1, 2], [3, 4]])
r = arr.ravel()
r[0] = 100
print(arr)   # arr changes if ravel gave a view