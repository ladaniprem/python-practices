#sorting data

#sorting data 1 column sort_values()
#df.sort_values(by='column_name',True/False,implace=True/False)

import pandas as pd

data = {
    'Name': ['Ram', 'Mohan', 'Chovan', 'Thovan'],
    'Age': [28, 24, 35, 30],
    'Salary': [50000, 60000, 55000, 65000]
}

df = pd.DataFrame(data)
print("Original DataFrame:",df ,sep="\n")
df.sort_values(by='Age', ascending=False, inplace=True)
print("Sorted DataFrame:",df ,sep="\n")

#output:
"""
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