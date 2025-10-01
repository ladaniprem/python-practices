#trspanding single element
import numpy as np

matrix = np.array([[1,2,3],
                   [4,5,6]]) # 2*3 matrix
vector = np.array([1,2,3]) # 1d array
#note:- yaha pe numpy ne 1,2,3 ko expland kar diya across each rows of the matrix


result = matrix + vector
print(result)