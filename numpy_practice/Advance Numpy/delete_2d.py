import numpy as np

arr_2d  = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
new_arr_2d = np.delete(arr_2d, 1,axis=0)  # Delete the second row (index 1)
print("Original 2D array:\n", arr_2d)
print("New 2D array after deletion:\n", new_arr_2d)

# Note :- The axis parameter specifies whether to delete a row (axis=0) or a column (axis=1).
#numpy remove karne ke liye implise jesa koy function nahi hai
#their provide a new array without the deleted element

