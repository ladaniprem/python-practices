#adding new columns
import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)

# .loc[]
# df.loc[row_index,"Column_Name"] = new_value
# df.loc[0,"Salary"] = 60000
# print(df)

#increasing salary by 10%

df['Salary'] =df['Salary'] * 1.1
print(df)

#output :- 
'''
> python -u "d:\prem\coding\code with python\pandas_practice\advance pandas\updating2.py"
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

     Name  Age   Salary
0    prem   25  55000.0
1    jeel   30  44000.0
2    meet   35  33000.0
3     het   28  22000.0
4     ram   32  11000.0
5    deep   27   5500.0
6   Harry   29   4400.0
7  sanjay   31   8800.0
8   samay   26   9900.0
9   jimit   33  13200.0
'''
