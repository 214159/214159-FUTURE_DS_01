import pandas as pd
excel_path=r"C:\\Users\\priya\\OneDrive\\Desktop\\archive\\superstore.xls"
df=pd.read_excel(excel_path)
print(df.head())
print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.duplicated().sum())
df['Order Date']=pd.to_datetime(df['Order Date'])
df['Revenue']=df['Sales']*(1-df['Discount'])
print(df.head())
df.to_csv("Superstore.csv",index=False)