import sqlite3
import os

def get_connection():
    # Get current file directory → scripts/app
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up TWO levels → BrickView
    project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

    # Build DB path → BrickView/db/real_estate.db
    db_path = os.path.join(project_root, "db", "real_estate.db")

    print("📂 Trying DB path:", db_path)

    # Check if file exists
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Database not found at: {db_path}")

    return sqlite3.connect(db_path)