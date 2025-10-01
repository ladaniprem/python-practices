#np.isinf(array) 10 ^1000
#1/0

import numpy as np

arr = np.array([1, 2, np.inf, -np.inf, 5])

print(np.isinf(arr))