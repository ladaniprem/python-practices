# tempratures = [32.5, 31.8, 29.5, 35.0, 30.0]

# total = 0 
# for temp in tempratures:
#     total += temp
#     average = total / len(tempratures)

# print("Average temperature is: ", average)

# numpy creator travis oliphant - 2005

import numpy as np

temperatures = np.array([32.5, 31.8, 29.5, 35.0, 30.0])
average  = np.mean(temperatures)
print("Average temperature is: ", average)

# large amount of data ko quickly process krna ho to numpy use krty hain
# numpy arrays are more efficient than lists in terms of memory and performance
# numpy fast hai 50-100 times zyada fast hai as compared to lists
# less memory use krty hain as compared to lists
# numpy arrays are homogenous - same data type
# easy mathematical operations kr sakty hain numpy arrays pr
# numpy arrays multidimensional ho sakty hain
# numpy arrays are widely used in data science and machine learning
# small data set use list and large data set use numpy arrays

