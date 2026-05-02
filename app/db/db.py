import sqlite3
from config import DB_PATH
try:
    with sqlite3.connect(DB_PATH) as conn:
        print("Connected to SQLite database")
        cursor = conn.cursor()
        cursor.execute("""CREATE TABLE IF NOT EXISTS receipt(
            id INTEGER PRIMARY KEY,
            date TEXT NOT NULL,
            negozio TEXT,
            category TEXT NOT NULL,
            total REAL NOT NULL
        );""")
        print("Table created successfully!")
except sqlite3.OperationalError as e:
    print("Failed to open database:", e)