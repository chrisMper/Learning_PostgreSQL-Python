from connection import engine
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#getting the data from the database
query = "SELECT * FROM store_sales;"
df = pd.read_sql(query, engine)

#total store sales
query = """
SELECT "StoreName", SUM("NetSales") as "TotalSales"
FROM store_sales
GROUP BY "StoreName"
ORDER BY "TotalSales" DESC;
"""
Total_store_sales = pd.read_sql(query, engine)

#plot the data
plt.figure(figsize=(10,6))
sns.barplot(
x="StoreName",
y="TotalSales",
data=Total_store_sales,
)

plt.title("Sales by Store")
plt.xlabel("Store Name")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
# Save the plot
plt.savefig("sales_by_store.png")
print("Bar chart saved as sales_by_store.png")
