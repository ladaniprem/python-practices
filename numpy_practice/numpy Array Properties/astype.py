#astype: changing the datatype of the array
import numpy as np

arr = np.array([1.2,2.5,4.7])
int_arr = arr.astype('int')
print(int_arr)
print(int_arr.dtype) # output [1 2 4] ,int64