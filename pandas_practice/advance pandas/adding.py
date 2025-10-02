#adding new columns
import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)

#square brackets df['column_name'] = some_Data

df['Bonus'] = df['Salary'] * 0.10
print(df)

#using insert()
#df.insert(loc,"column_name",same_data)
df.insert(0,"Employee Id:",[10,20,30,40,50,60,70,80,90,100])
print(df)

#output :- 
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

     Name  Age  Salary   Bonus
0    prem   25   50000  5000.0
1    jeel   30   40000  4000.0
2    meet   35   30000  3000.0
3     het   28   20000  2000.0
4     ram   32   10000  1000.0
5    deep   27    5000   500.0
6   Harry   29    4000   400.0
7  sanjay   31    8000   800.0
8   samay   26    9000   900.0
9   jimit   33   12000  1200.0

  Employee Id:    Name  Age  Salary   Bonus
0            10    prem   25   50000  5000.0
1            20    jeel   30   40000  4000.0
2            30    meet   35   30000  3000.0
3            40     het   28   20000  2000.0
4            50     ram   32   10000  1000.0
5            60    deep   27    5000   500.0
6            70   Harry   29    4000   400.0
7            80  sanjay   31    8000   800.0
8            90   samay   26    9000   900.0
9           100   jimit   33   12000  1200.0
"""