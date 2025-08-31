import pandas as pd

# Load CSV files
orders = pd.read_csv(r"C:\Users\archa\Desktop\Sales_Project\Orders.csv")
details = pd.read_csv(r"C:\Users\archa\Desktop\Sales_Project\Details.csv")

# Merge on common column
df = pd.merge(orders, details, on="Order ID")

# Cleaning
df.dropna(inplace=True) #remove null row
df.drop_duplicates(inplace=True)

# Convert date column to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'] , dayfirst=True)

# Save cleaned dataset (save in main project folder)
df.to_excel(r"C:\Users\archa\Desktop\Sales_Project\Cleaned_SalesData.xlsx", index=False)

print("Data cleaned and saved as Cleaned_SalesData.xlsx")
