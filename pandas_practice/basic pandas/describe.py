import pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

print("\nDescriptive Statistics:")
print(df.describe())


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

Descriptive Statistics:
             Age        Salary
count  10.000000     10.000000        
mean   29.600000  18800.000000        
std     3.204164  15970.806701        
min    25.000000   4000.000000        
25%    27.250000   8250.000000        
50%    29.500000  11000.000000        
75%    31.750000  27500.000000        
max    35.000000  50000.000000         
"""


