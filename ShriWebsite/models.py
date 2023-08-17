import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os
from dotenv import load_dotenv

load_dotenv()

db_url = os.environ.get('POSTGRES_USERSDB_URL')
db_user = os.environ.get('POSTGRES_USERSDB_USER')
db_host = os.environ.get('POSTGRES_USERSDB_HOST')
db_password = os.environ.get('POSTGRES_USERSDB_PASSWORD')
db_database = os.environ.get('POSTGRES_USERSDB_DATABASE')

def create_database(url=db_url):
    try:
        conn = psycopg2.connect(url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(f'CREATE DATABASE {db_database};')
        conn.commit()
        conn.close()
        return True
    except:
        return False

def create_table(table, columns, url=db_url):
    try:
        conn = psycopg2.connect(url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(f'CREATE TABLE IF NOT EXISTS {table} {columns};')
        conn.commit()
        conn.close()
        return True
    except:
        return False

def insert_data(data, url=db_url):
    try:
        conn = psycopg2.connect(url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(data)
        conn.commit()
        conn.close()
        return True
    except:
        return False
    
def get_data(query, url=db_url):
    try:
        conn = psycopg2.connect(url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(query)
        data = cur.fetchall()
        conn.close()
        return data
    except:
        return False
    
def update_data(query, url=db_url):
    try:
        conn = psycopg2.connect(url)
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
        conn.close()
        return True
    except:
        return False
