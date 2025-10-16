""" df["Coloumn Name"].mean()
df["Coloumn Name"].sum()
df["Coloumn Name"].min()
df["Coloumn Name"].max()
df["Coloumn Name"].std()
df["Coloumn Name"].count()
df["Coloumn Name"].median()
df["Coloumn Name"].var()
"""

import pandas as pd

data = {
    'Name': ['Ram', 'Mohan', 'Chovan', 'Thovan'],
    'Age': [28, 24, 35, 30],
    'Salary': [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
print("Original DataFrame:",df ,sep="\n")

avg_salary = df["Salary"].mean()
print("Average Salary:", avg_salary)

max_age = df['Age'].max()
print("Maximum Age:", max_age)

min_age = df['Age'].min()
print("Minimum Age:", min_age)

# Output :- 

"""
Original DataFrame:
     Name  Age  Salary
0     Ram   28   50000
1   Mohan   24   60000
2  Chovan   35   55000
3  Thovan   30   65000
Average Salary: 57500.0
Maximum Age: 35
Minimum Age: 24
"""