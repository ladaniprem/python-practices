df = pd.read_csv("sales_data_sample.csv", encoding='latin-1')
print("CSV data loaded successfully:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")


df = pd.read_excel("SampleSuperstore.xlsx")
print("Excel data loaded successfully:")
print(df.head())
print(f"\nDataFrame shape: {df.shape}")
print(f"Columns: {list(df.columns)}")