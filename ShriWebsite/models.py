import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

user = os.environ.get("USER")
password = os.environ.get("PASSWORD")
host = os.environ.get("HOST")
port = os.environ.get("PORT")
database = os.environ.get("DATABASE")
ssl_ca = os.environ.get("SSL_CA")
ssl_disabled = os.environ.get("SSL_DISABLED")

def create_table(table, columns):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_ca=ssl_ca,
            ssl_disabled=ssl_disabled
        )
        cur = conn.cursor()
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table} {columns};')
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False

def insert_data(insert_query, data):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_ca=ssl_ca,
            ssl_disabled=ssl_disabled
        )
        cur = conn.cursor()
        cur.execute(insert_query, data)
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    
def get_data(query):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_ca=ssl_ca,
            ssl_disabled=ssl_disabled
        )
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        conn.close()
        return data
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    
def update_data(update_query, data):
    try:
        conn = mysql.connector.connect(
            user=user,
            password=password,
            host=host,
            port=port,
            database=database,
            ssl_ca=ssl_ca,
            ssl_disabled=ssl_disabled
        )
        cur = conn.cursor()
        cur.execute(update_query, data)
        conn.commit()
        conn.close()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    