import pandas as pd
import sqlalchemy

# Load Cleaned Data
df = pd.read_excel(r"C:\Users\archa\Desktop\Sales_Project\Cleaned_SalesData.xlsx")

# SQL Connection (MySQL example)
engine = sqlalchemy.create_engine("mysql+pymysql://archana:mourya@localhost:3306/salesdb")

# Save to SQL
df.to_sql("orders_data", engine, index=False, if_exists="replace")

print("Data Loaded into MySQL Database (salesdb.orders_data)")
