import pandas as pd
df = pd.read_csv("dataset.txt", sep = ";", header = 0)
print(df)

columns = ["Companies"]
print( df.groupby(columns)["Quantity"].sum() )ny","Payment )


companies = {"Deloite & Touche": {"Cash": 0, "Credit": 0},
            "EY": {"Cash": 0, "Credit": 0},
            "KPMG": {"Cash": 0, "Credit": 0},
            "PWC": {"Cash": 0, "Credit": 0}}

for i in range(len(df)):
    Names, payment, quantity = dr.iloc[i]["Company"], dr.iloc[i]["Payment"], dr.iloc[i]["Quantity"]
    Companies[Names][payment] = quantity
    
    for key,value in Company_names.items():
    companyName = key

