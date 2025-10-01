#np.nan_to_num(array,nan=value) default- 0

import numpy as np

arr = np.array([1,2,np.nan,4,np.nan,6])

cleaned_arr = np.nan_to_num(arr,)
print(cleaned_arr)

#note output:- 
#PS D:\prem\coding\code with python>python -u "d:\prem\coding\code with python\numpy_practice\Handling Missing Values\nan_to_num.py"
# [ 1.  2. 60.  4. 60.  6.] by default it replaces nan with value
# PS D:\prem\coding\code with python>python -u "d:\prem\coding\code with python\numpy_practice\Handling Missing Values\nan_to_num.py"
# [ 1.  2.  0.  4.  0.  6.] by default it replaces nan with 0