#df.sort_values() method is used to sort a DataFrame by one or more columns.
#df.sort_values(by=['column_name1','column_name2'], ascending=True/False, inplace=True/False)
import pandas as pd

data = {
    'Name': ['Ram', 'Mohan', 'Chovan', 'Thovan'],
    'Age': [28, 24, 35, 30],
    'Salary': [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
print("Original DataFrame:",df ,sep="\n")
df.sort_values(by=['Age','Salary'], ascending=False, inplace=True)
print("Sorted DataFrame:",df ,sep="\n")

#output:
"""
ascending = True
Original DataFrame:
     Name  Age  Salary
0     Ram   28   50000
1   Mohan   24   60000
2  Chovan   35   55000
3  Thovan   30   65000
Sorted DataFrame:
     Name  Age  Salary
1   Mohan   24   60000
0     Ram   28   50000
3  Thovan   30   65000
2  Chovan   35   55000

ascending = False

Original DataFrame:
     Name  Age  Salary
0     Ram   28   50000
1   Mohan   24   60000
2  Chovan   35   55000
3  Thovan   30   65000
Sorted DataFrame:
     Name  Age  Salary
2  Chovan   35   55000
3  Thovan   30   65000
0     Ram   28   50000
1   Mohan   24   60000

"""