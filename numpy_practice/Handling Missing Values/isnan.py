#np.isnan(array)

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])
print(np.isnan(arr))  # Output: [False False  True False  True False]

print(np.nan == np.nan) # Output: False
#Note :- directly compare nahi karsakhte hai

