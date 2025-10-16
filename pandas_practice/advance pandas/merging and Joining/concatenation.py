"""
vertically (rows wise) concatenate two DataFrames using pd.concat() function.
Horizontally (column wise) concatenate two DataFrames using pd.concat() function.

pd.concat([df1,df2], axis=0,ignore_index=True)

[df1,df2] :- list of DataFrames to concatenate
axis=0 :- for vertical concatenation
axis=1 :- for horizontal concatenation
ignore_index=True :- to reindex the new DataFrame

"""

import pandas as pd

#region 1 data
df_region1 = pd.DataFrame({
    'CustomerID': [1, 2, 3],
    'Name': ['jay', 'ram', 'meet']
})

#region 2 data

df_region2 = pd.DataFrame({
    'CustomerID': [4, 5, 6],
    'Name': ['jeet', 'rit', 'smith']
})

#vertical concatenation

df_concatenated = pd.concat([df_region1, df_region2],axis=0, ignore_index=True)
print("Vertically Concatenated DataFrame:\n", df_concatenated)

#horizontal concatenation

df_concatenated = pd.concat([df_region1, df_region2], axis=1, ignore_index=True) 
print("Horizontally Concatenated DataFrame:\n", df_concatenated)

#output 

"""

Vertically Concatenated DataFrame:
    CustomerID   Name
0           1    jay
1           2    ram
2           3   meet
3           4   jeet
4           5    rit
5           6  smith

Horizontally Concatenated DataFrame:
    0     1  2      3
0  1   jay  4   jeet
1  2   ram  5    rit
2  3  meet  6  smith


"""