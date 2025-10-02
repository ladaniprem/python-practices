import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
#selecting single columns
print("Names(Single column return series)")
# print(df["Name"])
name = df['Name']
print(name)

#selecting multiple columns

sunset = df[["Name", "Salary"]]
print("Multiple columns return dataframe")
print(sunset)

#output :-
"""
Original DataFrame:
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
Names(Single column return series)    
0      prem
1      jeel
2      meet
3       het
4       ram
5      deep
6     Harry
7    sanjay
8     samay
9     jimit
Name: Name, dtype: object
Multiple columns return dataframe
     Name  Salary
0    prem   50000
1    jeel   40000
2    meet   30000
3     het   20000
4     ram   10000
5    deep    5000
6   Harry    4000
7  sanjay    8000
8   samay    9000
9   jimit   12000

"""