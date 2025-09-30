#numpy 0 base indexing ko follow krta hai
#numpy postive and negative indexing dono ko support krta hai
#array[index] 1d array
#array[row_index, column_index] 2d array

import numpy as np

arr = np.array([10,20,30,40,50])

print(arr[0]) #first element
print(arr[2]) #30 0 based indexing
print(arr[-1]) #last element
print(arr[-3]) #30


