#incompatible shapes

import numpy as np

arr1 = np.array([[1,2,3],
                 [4,5,6]]) # 2*3 matrix
arr2 = np.array([1,2]) # 1d array
#note:- yaha pe numpy ne 1,2 ko 3 columns me fit nahi kar paya isliye error aaya
result = arr1 + arr2
print(result)
"""
error show its like this:-
Traceback (most recent call last):
  File "d:\prem\coding\code with python\numpy_practice\Brodcasting\error.py", line 9, in <module>
    result = arr1 + arr2
             ~~~~~^~~~~~
ValueError: operands could not be broadcast together with shapes (2,3) (2,) 
"""
# solution:- make the shapes compatible using .reshape() or np.newaxis

