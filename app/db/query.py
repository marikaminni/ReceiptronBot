import sqlite3
from config import DB_PATH

"""Save parsed data to DB"""
def save_receipt(data: dict) -> int|None:
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

"""Filter data based to n month, weeks or days"""
def filter_period(n:int) -> list| None:
    subtrahend = f"-{n} days"
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            cur= conn.cursor()
            cur.execute("""
            SELECT category, SUM(total) as Total
            FROM receipt
            WHERE date >= date('now', ?)
            GROUP BY category
            ORDER BY date ASC
            """, (subtrahend,))

            rows = cur.fetchall()
            print("Retrieved data:", rows)
            return rows

    except sqlite3.OperationalError as e:
        print("Failed to open database: ", e)
    except sqlite3.Error as err:
        print("Failed to fetch data: ", err)
