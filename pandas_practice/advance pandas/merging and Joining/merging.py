#pd.merge(df1,df2,on='column_name',how='inner/outer/left/right')

import pandas as pd

#customer dataframe
df_customer = pd.DataFrame({
    'CustomerID': [1, 2, 3, 4],
    'Name': ['Ram', 'Mohan', 'Chovan', 'Thovan'],
})

#order dataframe

df_order = pd.DataFrame({
    'CustomerID': [1, 2, 3, 5],
    'OrderAmount': [250, 450, 300, 150]
})

#merging dataframes

#inner join
df_merged = pd.merge(df_customer,df_order,on='CustomerID',how='inner')
print("inner join :\n",df_merged)

#outer join
df_merged = pd.merge(df_customer,df_order,on='CustomerID',how='outer')
print("outer join :\n",df_merged)

#left join
df_merged = pd.merge(df_customer,df_order,on='CustomerID',how='left')
print("left join :\n",df_merged)

#right join
df_merged = pd.merge(df_customer,df_order,on='CustomerID',how='right')
print("right join :\n",df_merged)

#output
"""
inner join :
    CustomerID    Name  OrderAmount
0           1     Ram          250
1           2   Mohan          450
2           3  Chovan          300

outer join :
    CustomerID    Name  OrderAmount
0           1     Ram        250.0
1           2   Mohan        450.0
2           3  Chovan        300.0
3           4  Thovan          NaN
4           5     NaN        150.0

left join :
    CustomerID    Name  OrderAmount
0           1     Ram        250.0
1           2   Mohan        450.0
2           3  Chovan        300.0
3           4  Thovan          NaN

right join :
    CustomerID    Name  OrderAmount
0           1     Ram          250
1           2   Mohan          450
2           3  Chovan          300
3           5     NaN          150

"""

"""
Note :- 

1df = m rows
2df = n rows
m * n = total rows in merged dataframe

"""