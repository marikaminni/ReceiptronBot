import sqlite3
from config import DB_PATH
def init_db():
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

def save_receipt(data: dict) -> int:
    try:
        with sqlite3.connect(DB_PATH) as conn:
            cur= conn.cursor()
            cur.execute("""
            INSERT INTO receipt (date, negozio, category, total)
            VALUES (:date, :negozio, :category, :total)""", data)

            print("Insertion was successful!")

            #get the id of the last inserted row
            return cur.lastrowid
    except sqlite3.OperationalError as e:
        print("Failed to open database:", e)