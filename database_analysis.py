import pandas as pd
from sqlalchemy import create_engine, text

# Database connection credentials
USERNAME = "postgres"
PASSWORD = "admin"  # Replace with your actual password if different
HOST = "localhost"
PORT = "5432"
DB_NAME = "store_performance_db"

# Create the connection engine (Don't forget the password in the connection string!)
engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")

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
