#Q2. Implement a context manager to handle database transactions (e.g., commit, rollback) using Python's contextlib module.

import contextlib
import sqlite3

@contextlib.contextmanager
def transaction_manager(conn):
    try:
        yield
        conn.commit()
    except Exception as e:
        conn.rollback()
        raise e

conn = sqlite3.connect('mydb.db')
with transaction_manager(conn):
    cursor = conn.cursor()
  
    cursor.execute('CREATE TABLE IF NOT EXISTS table_name (column1 TEXT)')
    
    cursor.execute('INSERT INTO table_name (column1) VALUES (?)', ('hello',))

with conn:
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM table_name')
    rows = cursor.fetchall()
    for row in rows:
        print(row)

conn.close()
