import pandas as pd


# Read CSV file with latin-1 encoding to handle special characters
df = pd.read_csv("pandas_practice/sales_data_sample.csv", encoding='latin-1')
print("CSV data loaded successfully:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")


df = pd.read_excel("pandas_practice/SampleSuperstore.xlsx")
print("Excel data loaded successfully:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")

df = pd.read_json("pandas_practice/sample_Data.json")
print("JSON data loaded successfully:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")


#Note :- cloud storage pe data store krke rakha ho to use the gcsfs library to read the data from there.
# import gcsfs

#output:- 
"""
CSV data loaded successfully:
   ORDERNUMBER  ...  DEALSIZE
0        10107  ...     Small  
1        10121  ...     Small  
2        10134  ...    Medium  
3        10145  ...    Medium  
4        10159  ...    Medium  

[5 rows x 25 columns]

DataFrame shape: (2823, 25)    
Columns: ['ORDERNUMBER', 'QUANTITYORDERED', 'PRICEEACH', 'ORDERLINENUMBER', 'SALES', 'ORDERDATE', 'STATUS', 'QTR_ID', 'MONTH_ID', 'YEAR_ID', 'PRODUCTLINE', 'MSRP', 'PRODUCTCODE', 'CUSTOMERNAME', 'PHONE', 'ADDRESSLINE1', 'ADDRESSLINE2', 'CITY', 'STATE', 'POSTALCODE', 'COUNTRY', 'TERRITORY', 'CONTACTLASTNAME', 'CONTACTFIRSTNAME', 'DEALSIZE']
Excel data loaded successfully:
   Row ID  ...    Profit
0       1  ...   41.9136       
1       2  ...  219.5820       
2       3  ...    6.8714       
3       4  ... -383.0310       
4       5  ...    2.5164       

[5 rows x 21 columns]

DataFrame shape: (9994, 21)    
Columns: ['Row ID', 'Order ID', 'Order Date', 'Ship Date', 'Ship Mode', 'Customer ID', 'Customer Name', 'Segment', 'Country', 'City', 'State', 'Postal Code', 'Region', 'Product ID', 'Category', 'Sub-Category', 'Product Name', 'Sales', 'Quantity', 'Discount', 'Profit']
JSON data loaded successfully:
   id  ...                     
                         image 
0   1  ...  https://www.apple.com/newsroom/images/product/... 
1   2  ...  https://images.samsung.com/is/image/samsung/p6... 
2   3  ...  https://www.sony.com/image/44baa604124b770c824... 
3   4  ...  https://www.lg.com/us/images/tvs/md07501804/ga... 
4   5  ...  https://assets.bose.com/content/dam/Bose_DAM/W... 

[5 rows x 6 columns]

DataFrame shape: (20, 6)       
Columns: ['id', 'name', 'description', 'price', 'category', 'image']

"""