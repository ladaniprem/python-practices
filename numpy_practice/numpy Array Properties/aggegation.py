#aggregation operations use in numpy array like sum, min, max, mean, median, std, var etc

import numpy as np

arr = np.array([[1,2,3],
                [4,5,6]])
print(np.sum(arr))  #sum of all elements
print(np.sum(arr, axis=0))  #sum of each column
print(np.sum(arr, axis=1))  #sum of each row
print(np.min(arr))  #minimum element
print(np.max(arr))  #maximum element
print(np.mean(arr))  #mean of all elements
print(np.median(arr))  #median of all elements
print(np.std(arr))  #standard deviation of all elements
print(np.var(arr))  #variance of all elements
print(np.argmin(arr))  #index of minimum element
print(np.argmax(arr))  #index of maximum element
print(np.percentile(arr, 50))  #50th percentile (median)
print(np.percentile(arr, 90))  #90th percentile
print(np.cumsum(arr))  #cumulative sum of elements
print(np.cumprod(arr))  #cumulative product of elements
print(np.cumprod(arr, axis=0))  #cumulative product of each column
print(np.cumprod(arr, axis=1))  #cumulative product of each row
print(np.cumprod(arr, dtype=np.float64))  #cumulative product with specified dtype
print(np.cumprod(arr, axis=0, dtype=np.float64))  #cumulative product of each column with specified dtype
print(np.cumprod(arr, axis=1, dtype=np.float64))  #cumulative product of each row with specified dtype