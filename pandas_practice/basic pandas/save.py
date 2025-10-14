import pandas as pd

data = {
    "Name":['prem','ram','shyam'], 
    "Age": [24,25,26],
    "city":['delhi','noida','gurgaon']
}
df = pd.DataFrame(data)
print(df)

# df.to_csv("output.csv",index=False)
# df.to_excel("output.xlsx",index=False)
# df.to_json("output.json",index=False)

#output same output differnt formate:-
"""
   Name  Age    city
0   prem   24   delhi
1    ram   25   noida   
2  shyam   26  gurgaon
"""