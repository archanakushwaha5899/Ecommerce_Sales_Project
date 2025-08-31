import matplotlib.pyplot as plt
import seaborn as sns
import os
from sales_analysis import top_states, category_sales, monthly_sales, payment_mode, top_products, city_sales, monthly_growth

# create folder if not exists
os.makedirs("outputs", exist_ok=True)

# --- Bar Chart: Top 10 States by Sales

def plot_states():
    df_state = top_states()
    sns.barplot(x='STATE', y='TotalSales', data=df_state, palette='Blues_d')
    plt.title("Top 5 States by Total Sales")
    plt.savefig("outputs/top_states.png")
    plt.show()

# --- Pie Chart: Category-wise Sales Distribution

def plot_category():
    df_category = category_sales()
    plt.pie(df_category['TotalSales'], labels=df_category['category'], autopct='%1.1f%%', startangle=140)
    plt.title("Category-wise Sales Distribution")
    plt.savefig("outputs/category_sales.png")
    plt.show()

# --- Line Chart: Monthly Sales Trend

def plot_monthly():
    df_month = monthly_sales()
    sns.lineplot(x='Month', y='TotalSales', data=df_month, marker='o')
    plt.title("Monthly Sales Trend")
    plt.xticks(rotation=45)
    plt.savefig("outputs/monthly_sales.png")
    plt.show()

 # --- Bar Chart: Payment Mode Analysis

def plot_payment():
    df_payment = payment_mode()
    sns.barplot(x='PaymentMode', y='TotalSales', data=df_payment, palette='Set2')
    plt.title("Payment Mode Analysis")
    plt.savefig("outputs/payment_mode.png")
    plt.show()

 # --- Bar Chart: Top Products

def plot_products():
    df_product = top_products()
    sns.barplot(x='Product', y='TotalSales', data=df_product, palette='Set2')
    plt.title("Top 10 Products by Sales")
    plt.xticks(rotation=45)
    plt.savefig("outputs/top_products.png")
    plt.show()

 # --- Bar Chart: Cities Wise Sales

def plot_city_sales():
    df_city = city_sales()
    sns.barplot(x='City', y='TotalSales', data=df_city, palette='viridis')
    plt.title("Top 10 Cities by Sales")
    plt.xticks(rotation=45)
    plt.savefig("outputs/city_sales.png")
    plt.show()

# --- Line Chart: Monthly Growth

def plot_monthly_growth():
    df_month_growth = monthly_growth()
    sns.lineplot(x='Month', y='Growth%', data=df_month_growth, marker='o')
    plt.title("Month-over-Month Growth (%)")
    plt.xticks(rotation=45)
    plt.savefig("outputs/monthly_growth.png")
    plt.show()


if __name__ == "__main__":
    # Test run (direct run karoge to ye chalega)

    print("---------Top 5 State By Sales----------- ")
    print(top_states())
    plot_states()
    
    print("---------Categories Wise Sales-----------")
    print(category_sales())
    plot_category()

    print("---------Monthly Sales Trend-------------")
    print(monthly_sales())
    plot_monthly()

    print("---------Sales according to Pyment-------")
    print(payment_mode())
    plot_payment()

    print("---------Top Product-----------")
    print(top_products())
    plot_products()

    print("---------City Wise Sales-------------")
    print(city_sales())
    plot_city_sales()

    print("---------Monthly Growth-------")
    print(monthly_growth())
    plot_monthly_growth()

    