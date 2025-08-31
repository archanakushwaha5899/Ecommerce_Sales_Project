import pandas as pd
import sqlalchemy

# Database connection
engine = sqlalchemy.create_engine("mysql+pymysql://archana:mourya@localhost:3306/salesdb")


#--------------Top 10 States by Sales
def top_states():
    query = """
    SELECT STATE, SUM(Amount) AS TotalSales
    FROM orders_data
    GROUP BY STATE
    ORDER BY TotalSales DESC
    LIMIT 10;
    """
    df = pd.read_sql(query, engine)
    return df

#--------------Category-wise Sales Distribution
def category_sales():
    query = """
    SELECT category, SUM(Amount) AS TotalSales, SUM(Quantity) AS TotalQuantity
    FROM orders_data
    GROUP BY category
    ORDER BY TotalSales DESC;
    """
    df = pd.read_sql(query, engine)
    return df

#---------------Monthly Sales Trend

def monthly_sales():
   query = """
       SELECT DATE_FORMAT(`Order Date`, '%%Y-%%m') AS Month,
       SUM(Amount) AS TotalSales
       FROM orders_data
       GROUP BY DATE_FORMAT(`Order Date`, '%%Y-%%m')
       ORDER BY DATE_FORMAT(`Order Date`, '%%Y-%%m');
       """
   df = pd.read_sql(query, engine)
   return df

#-------------------Payment Mode Analysis

def payment_mode():
    query = """
    SELECT PaymentMode, COUNT(*) AS TotalOrders, SUM(Amount) AS TotalSales
    FROM orders_data
    GROUP BY PaymentMode;
    """
    df = pd.read_sql(query, engine)
    return df

#----------------Top 10 Products by Sales

def top_products():
    query ="""
    SELECT `Sub_Category` AS Product, SUM(Amount) AS TotalSales
    FROM orders_data
    GROUP BY `Sub_Category`
    ORDER BY TotalSales DESC
    LIMIT 10;
    """

    df = pd.read_sql(query,engine)
    return df


#-----------------City-wise Sales Performance

def city_sales():
    query="""
    SELECT City, SUM(Amount) AS TotalSales
    FROM orders_data
    GROUP BY City
    ORDER BY TotalSales DESC
    LIMIT 10;
    """

    df = pd.read_sql(query,engine)
    return df

# --- Month-over-Month Growth %

def monthly_growth():
    query = """
    SELECT DATE_FORMAT(`Order Date`, '%%Y-%%m') AS Month,
           SUM(Amount) AS TotalSales
    FROM orders_data
    GROUP BY DATE_FORMAT(`Order Date`, '%%Y-%%m')
    ORDER BY Month;
    """
    df = pd.read_sql(query, engine)
    df['Growth%'] = df['TotalSales'].pct_change() * 100
    return df