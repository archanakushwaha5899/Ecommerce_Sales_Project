import sqlalchemy
from sqlalchemy import text
import pandas as pd


#MySQL Connection
engine = sqlalchemy.create_engine("mysql+pymysql://archana:mourya@localhost:3306/salesdb")

# Check tables
with engine.connect() as con:
    tables = con.execute(text("SHOW TABLES;"))
    print([table[0] for table in tables])

# Read few rows
df = pd.read_sql("SELECT * FROM orders_data LIMIT 5;", engine)
print(df)   

    