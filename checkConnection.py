#Check the connection
import pandas as pd
from sqlalchemy import text
from connection import engine

#create a function for check enitre table
def check_entire_table():
    with engine.connect() as conn:
        count = conn.execute(text("SELECT COUNT(*) FROM store_sales;"))
        print("-"*50)
        print("Connected! Number of rows in the table:", count.fetchone()[0])
        print("-"*50)
