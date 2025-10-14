#adding new columns
import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)

#df.drop(columns=["column_name"], inplace=True) #removing column
print("\nAfter removing column Name\n")
df.drop(columns=['Name'], inplace=True)
# df.drop(columns=['Name', 'Age'], inplace=True)
print(df)

#output
'''
 python -u "d:\prem\coding\code with python\pandas_practice\advance pandas\removing.py"
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

After removing column Name        

   Age  Salary
0   25   50000
1   30   40000
2   35   30000
3   28   20000
4   32   10000
5   27    5000
6   29    4000
7   31    8000
8   26    9000
9   33   12000

After removing column Name        

   Salary
0   50000
1   40000
2   30000
3   20000
4   10000
5    5000
6    4000
7    8000
8    9000
9   12000
'''
