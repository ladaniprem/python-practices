#adding new columns
import pandas as pd

data = {
     'Name': ['prem', None, 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, None, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,None,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)

print(df.isnull())
print(df.isnull().sum())


#output :- 
'''
> python -u "d:\prem\coding\code with python\pandas_practice\advance pandas\Handling Missing Data\missing.py"
     Name   Age   Salary
0    prem  25.0  50000.0
1    None   NaN      NaN
2    meet  35.0  30000.0
3     het  28.0  20000.0
4     ram  32.0  10000.0
5    deep  27.0   5000.0
6   Harry  29.0   4000.0
7  sanjay  31.0   8000.0
8   samay  26.0   9000.0
9   jimit  33.0  12000.0

    Name    Age  Salary
0  False  False   False
1   True   True    True
2  False  False   False
3  False  False   False
4  False  False   False
5  False  False   False
6  False  False   False
7  False  False   False
8  False  False   False
9  False  False   False

Name      1
Age       1
Salary    1
dtype: int64
''' 

