import sqlite3
import os

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
db_path = os.path.join(BASE_DIR, "db", "real_estate.db")

def add_listing(data):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO listings 
    (Listing_ID, Address, City, State, Zip, Property_Type, Price, Area_sqft, Agent_ID, Listed_Date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, data)

    conn.commit()
    conn.close()

def delete_listing(listing_id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM listings WHERE Listing_ID=?", (listing_id,))
    conn.commit()
    conn.close()