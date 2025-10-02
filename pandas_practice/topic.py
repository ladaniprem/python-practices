"""
1- how big is your dataset?
2- what are the names of columns

Shape and Columns
"""

import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)
print(f"shape:{df.shape}")
print(f"columns:{df.columns}")
print(f"columns:{df.columns.tolist()}")


#output
"""
     Name  Age  Salary
0    prem   25   50000
1    jeel   30   40000
2    meet   35   30000
3     het   28   20000
4     ram   32   10000
5    deep   27    5000
6   Harry   29    4000
7  sanjay   31    8000
8   samay   26    9000
9   jimit   33   12000
shape:(10, 3)
columns:Index(['Name', 'Age', 'Salary'], dtype='object')
columns:['Name', 'Age', 'Salary']   

"""