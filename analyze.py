import pandas as pd
from sqlalchemy import text
from connection import engine
from checkConnection import check_entire_table

# Check the connection
check_entire_table()

# Get the data from the database
query = "SELECT * FROM store_sales;"
df = pd.read_sql(query, engine)

# print(df.head())

# print(df.shape)

# print(df.info())

#Display the stores with the higest sales
store_sales = (
 df.groupby("StoreName")["NetSales"]
 .sum()
 .sort_values(ascending=False)
 .head()
)
print("Store with highest sales:", store_sales)
#print a horizontal line
print("-"*50)

#Display the sales by region
region_sales = (
    df.groupby("Region")["NetSales"]
    .sum()
    .sort_values(ascending=False)
    .head()
)
print("Sales by region:", region_sales)
print("-"*50)

#Which days perform most revenue
revenue_days = (
    df.groupby("DayOfWeek")["NetSales"]
    .sum()
    .sort_values(ascending=False)
)
print("Revenue by day of week:", revenue_days)
print("-"*50)







