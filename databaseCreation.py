import pandas as pd
from sqlalchemy import text
from connection import engine
from checkConnection import check_entire_table

def test_connection():
    try:
        # Test the connection by getting the PostgreSQL version
        with engine.connect() as conn:
            result = conn.execute(text("SELECT version();"))
            print("Successfully connected to PostgreSQL!")
            print("PostgreSQL Version Details:")
            print(result.fetchone()[0])
            
    except Exception as e:
        print("Failed to connect to the database. Error details:")
        print(e)

if __name__ == "__main__":
    test_connection()

# Read the CSV file
store_df = pd.read_csv("store_performance_dataset.csv")

print("Original Data:")
print(store_df.head())

# Format the Date column
try:
    # Convert to datetime
    store_df['Date'] = pd.to_datetime(store_df['Date'])
    
    # Format as YYYY-MM-DD (or change to your preferred format)
    store_df['Date'] = store_df['Date'].dt.strftime('%Y-%m-%d')
    
    print("\nData after formatting Date:")
    print(store_df.head())
except Exception as e:
    print("\nError formatting date column:", e)
    print("Note: If the file literally contains '########', you will need to clean the data first.")

#uploading the data into the database
store_df.to_sql("store_sales", engine, if_exists="replace", index=False)
print("\nData uploaded to PostgreSQL successfully!")

#Check the connection
check_entire_table()

# Note: Project files have been restructured. Connection logic is now in connection.py
