#function:- selecting mutiple elements at once 

import numpy as np

arr = np.array([10,20,30,40,50,60,70,80,90])

print(arr[[0,2,4]]) # selecting 1st,3rd and 5th element copy to output provding it as list

print(arr[arr>50]) # selecting all elements greater than 50

