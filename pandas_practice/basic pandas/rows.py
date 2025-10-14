"""
PANDAS HEAD() AND TAIL() METHODS - THEORY AND EXAMPLES

head() method:
- Returns the first n rows of a DataFrame or Series
- Default n = 5 (shows first 5 rows)
- Syntax: df.head(n) where n is the number of rows
- Useful for quick data inspection and understanding structure

tail() method:
- Returns the last n rows of a DataFrame or Series  
- Default n = 5 (shows last 5 rows)
- Syntax: df.tail(n) where n is the number of rows
- Useful for checking the end of dataset and recent entries

Common use cases:
1. Data exploration - Quick peek at data structure
2. Data validation - Check if data loaded correctly
3. Debugging - Verify data transformations
4. Sampling - Get representative samples from large datasets
"""

import pandas as pd

#Create sample data for demonstration
# data = {
#     'Name': ['prem', 'jeel', 'meet', 'het', 'ram', 'deep', 'Harry', 'sanjay', 'samay', 'jimit'],
#     'Age': [25, 30, 35, 28, 32, 27, 29, 31, 26, 33],
#     'City': ['Ahemedabad', 'Rajkot', 'Rajkot', 'Ahmedabad', 'Surat', 'Vadodara', 'bharuch', '', 'Mumbai', 'vapi'],
#     'Salary': [50000, 60000, 70000, 55000, 65000, 58000, 62000, 68000, 52000, 72000]
# }  

# df = pd.DataFrame(data)
df = pd.read_json("pandas_practice/sample_Data.json")

print("display 10 rows of first:")
print(df.head())

print("display 10 rows of tail:")
print(df.tail())


# print("Original DataFrame:")
# print(df)
# print("\n" + "="*50 + "\n")

# # head() examples
# print("1. Default head() - First 5 rows:")
# print(df.head())
# print("\n" + "-"*30 + "\n")

# print("2. head(3) - First 3 rows:")
# print(df.head(3))
# print("\n" + "-"*30 + "\n")

# print("3. head(7) - First 7 rows:")
# print(df.head(7))
# print("\n" + "="*50 + "\n")

# # tail() examples
# print("4. Default tail() - Last 5 rows:")
# print(df.tail())
# print("\n" + "-"*30 + "\n")

# print("5. tail(3) - Last 3 rows:")
# print(df.tail(3))
# print("\n" + "-"*30 + "\n")

# print("6. tail(4) - Last 4 rows:")
# print(df.tail(4))
# print("\n" + "="*50 + "\n")

# # Practical examples
# print("7. Checking data after sorting:")
# df_sorted = df.sort_values('Salary', ascending=False)
# print("Highest salaries (head after sorting):")
# print(df_sorted.head(3))
# print("\nLowest salaries (tail after sorting):")
# print(df_sorted.tail(3))
# print("\n" + "="*50 + "\n")

# # Working with Series
# print("8. head() and tail() with Series:")
# ages = df['Age']
# print("First 3 ages:", ages.head(3).tolist())
# print("Last 3 ages:", ages.tail(3).tolist()) 


#output :- first orginal

"""
display 10 rows of first:
   id  ...                     
                         image 
0   1  ...  https://www.apple.com/newsroom/images/product/... 
1   2  ...  https://images.samsung.com/is/image/samsung/p6... 
2   3  ...  https://www.sony.com/image/44baa604124b770c824... 
3   4  ...  https://www.lg.com/us/images/tvs/md07501804/ga... 
4   5  ...  https://assets.bose.com/content/dam/Bose_DAM/W... 

[5 rows x 6 columns]
display 10 rows of tail:       
    id  ...                    
                          image
15  16  ...  https://www.breville.com/content/dam/breville/...
16  17  ...  https://www.keurig.com/content/dam/global-ecom...
17  18  ...  https://store.irobot.com/default/i7-vacuuming-...
18  19  ...  https://www.ninjakitchen.com/static/img/produc...
19  20  ...  https://www.cuisinart.com/share/images/product...

[5 rows x 6 columns]
"""

#output :-  updated code :-

"""
Original DataFrame:
     Name  ...  Salary
0    prem  ...   50000
1    jeel  ...   60000
2    meet  ...   70000
3     het  ...   55000
4     ram  ...   65000
5    deep  ...   58000
6   Harry  ...   62000
7  sanjay  ...   68000
8   samay  ...   52000
9   jimit  ...   72000

[10 rows x 4 columns]

==================================================

1. Default head() - First 5 rows:
   Name  ...  Salary
0  prem  ...   50000
1  jeel  ...   60000
2  meet  ...   70000
3   het  ...   55000
4   ram  ...   65000

[5 rows x 4 columns]

------------------------------ 

2. head(3) - First 3 rows:     
   Name  ...  Salary
0  prem  ...   50000
1  jeel  ...   60000
2  meet  ...   70000

[3 rows x 4 columns]

------------------------------ 

3. head(7) - First 7 rows:     
    Name  ...  Salary
0   prem  ...   50000
1   jeel  ...   60000
2   meet  ...   70000
3    het  ...   55000
4    ram  ...   65000
5   deep  ...   58000
6  Harry  ...   62000

[7 rows x 4 columns]

==================================================

4. Default tail() - Last 5 rows:
     Name  ...  Salary
5    deep  ...   58000
6   Harry  ...   62000
7  sanjay  ...   68000
8   samay  ...   52000
9   jimit  ...   72000

[5 rows x 4 columns]

------------------------------ 

5. tail(3) - Last 3 rows:      
     Name  Age    City  Salary
7  sanjay   31           68000 
8   samay   26  Mumbai   52000 
9   jimit   33    vapi   72000 

------------------------------ 

6. tail(4) - Last 4 rows:      
     Name  ...  Salary
6   Harry  ...   62000
7  sanjay  ...   68000
8   samay  ...   52000
9   jimit  ...   72000

[4 rows x 4 columns]

==================================================

7. Checking data after sorting:
Highest salaries (head after sorting):
     Name  Age    City  Salary 
9   jimit   33    vapi   72000 
2    meet   35  Rajkot   70000 
7  sanjay   31           68000 

Lowest salaries (tail after sorting):
    Name  ...  Salary
3    het  ...   55000
8  samay  ...   52000
0   prem  ...   50000

[3 rows x 4 columns]

==================================================

8. head() and tail() with Series:
First 3 ages: [25, 30, 35]     
Last 3 ages: [31, 26, 33]    

"""