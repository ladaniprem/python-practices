import pandas as pd

data = {
    "Time": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Value": [3, None, None, 8, 10, None, 12, None, 14, 16]
}


df = pd.DataFrame(data)
print("Before Interpolation\n", df)

df['Value'] = df["Value"].interpolate(method='linear')
print("After Interpolation\n", df)

#output
'''
PS D:\prem\coding\code with python> python -u "d:\prem\coding\code with python\pandas_practice\advance pandas\Handling Missing Data\linear.py"
Before Interpolation
    Time  Value
0     1    3.0
1     2    NaN
2     3    NaN
3     4    8.0
4     5   10.0
5     6    NaN
6     7   12.0
7     8    NaN
8     9   14.0
9    10   16.0

After Interpolation
    Time      Value
0     1   3.000000
1     2   4.666667
2     3   6.333333
3     4   8.000000
4     5  10.000000
5     6  11.000000
6     7  12.000000
7     8  13.000000
8     9  14.000000
9    10  16.000000
'''