import numpy as np

arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr_2d)
#insert a new row at index 1

# new_arr_2d = np.insert(arr_2d,1,[4,5,6],axis=1)
# new_arr_2d = np.insert(arr_2d,1,[10,11,12],axis=0)
new_arr_2d = np.insert(arr_2d,1,[10,11,12],axis=None)
print(new_arr_2d)