import pandas as pd

data = {
     'Name': ['prem', 'john', 'meet', 'het', 'ram', 'deep', 'Harry', 'steve', 'sam', 'james'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,40000,30000,20000,10000,5000,4000,8000,9000,12000],
     'Performance_Score':[96,67,90,56,87,56,45,34,35,56]
 }

df = pd.DataFrame(data)

high_salary = df[df['Salary']>40000]
print('Employees with salary>40000:')
print(high_salary)

#filtering rows Salary>40k & age>20

filtered = df[(df['Age']>20)&(df['Salary']>40000)]
print('Employees list Age>20 + Salary>40000')
print(filtered)

#using OR condition

filtered_or = df[(df['Age']>25) | (df['Performance_Score']>90)]
print('Employees list Age>25 + Performance_Score>90')
print(filtered_or)
  
#output 
"""
Employees with salary>40000:
   Name  Age  Salary
0  prem   25   50000

Employess list Age>20 + Salary>40000  
   Name  Age  Salary
0  prem   25   50000

Employees list Age>25 + Performance_Score>90
    Name  Age  Salary  Performance_Score
0   prem   25   50000                 96
1   john   30   40000                 67
2   meet   35   30000                 90
3    het   28   20000                 56
4    ram   32   10000                 87
5   deep   27    5000                 56
6  Harry   29    4000                 45
7  steve   31    8000                 34
8    sam   26    9000                 35
9  james   33   12000                 56

"""