
import pandas as pd

data = {
     'Name': ['prem','jeet', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
     'Age': [25, None, 35, 28, 32, 27, 29, 31, 26, 33],
     'Salary': [50000,None,30000,20000,10000,5000,4000,8000,9000,12000]
 }
df = pd.DataFrame(data)
print(df)

df.interpolate(method='linear',axis=0,inplace=True)