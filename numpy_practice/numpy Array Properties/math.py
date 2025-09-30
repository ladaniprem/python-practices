#operations on numpy array
import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
print(arr +5)
print(arr -5)
print(arr *5)
print(arr /5)
print(arr //5)
print(arr **2)

#output :-
# [[ 6  7  8]
#  [ 9 10 11]]
# [[-4 -3 -2]
#  [-1  0  1]]
# [[ 5 10 15]
#  [20 25 30]]
# [[0.2 0.4 0.6]       
#  [0.8 1.  1.2]]      
# [[0 0 0]
#  [0 1 1]]
# [[ 1  4  9]
#  [16 25 36]]