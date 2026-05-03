from db_connection import get_connection

conn = get_connection()
print("✅ Connected successfully")

cursor = conn.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

conn.close()