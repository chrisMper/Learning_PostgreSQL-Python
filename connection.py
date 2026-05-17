from sqlalchemy import create_engine

# Database connection credentials
USERNAME = "postgres"
PASSWORD = "admin"  # Replace with your actual password if different
HOST = "localhost"
PORT = "5432"
DB_NAME = "store_performance_db"

# Create the connection engine
engine = create_engine(f"postgresql+psycopg2://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}")
