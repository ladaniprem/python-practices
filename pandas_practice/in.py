import  pandas as pd

data = {
     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
     'City': ['Ahemedabad', 'Rajkot', 'Rajkot', 'Ahmedabad', 'Surat', 'Vadodara', 'bharuch', '', 'Mumbai', 'vapi'],
 }
#df = pd.read_json("pandas_practice/sample_Data.json")
df = pd.DataFrame(data)
print('display the info of data set:')
print(df.info())

# output :- 
"""
RangeIndex: 20 entries, 0 to 19
Data columns (total 6 columns):
 #   Column       Non-Null Count  Dtype
---  ------       --------------  -----
 0   id           20 non-null     int64
 1   name         20 non-null     object
 2   description  20 non-null     object
 3   price        20 non-null     float64
 4   category     20 non-null     object
 5   image        20 non-null     object
dtypes: float64(1), int64(1), object(4)
memory usage: 1.1+ KB
None

"""

#output of df :-
"""
display the info of data set:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 10 entries, 0 to 9 
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   Name    10 non-null     object
 1   Age     10 non-null     int64
 2   City    10 non-null     object
dtypes: int64(1), object(2)    
memory usage: 372.0+ bytes     
None
"""