import sqlite3
import os
import logging
from config.settings import DB_PATH

# Configure logging
logging.basicConfig(level=logging.INFO)

# Function to get the database connection
def get_db_connection():
    if not os.path.exists(DB_PATH):
        raise FileNotFoundError(f"Database file not found at: {DB_PATH}")
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        logging.error(f"Error connecting to the database: {e}")
        return None

# Function to initialize the database schema
def initialize_database():
    try:
        conn = get_db_connection()
        if not conn:
            raise ConnectionError("Failed to establish a database connection.")
        conn.executescript('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER UNIQUE,
            language TEXT DEFAULT 'en'
        );

        CREATE TABLE IF NOT EXISTS quizzes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            data TEXT
        );

        CREATE TABLE IF NOT EXISTS scores (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            quiz_id INTEGER,
            score INTEGER
        );
        ''')
        conn.commit()
        logging.info("Database initialized successfully.")
    except sqlite3.Error as e:
        logging.error(f"An error occurred while initializing the database: {e}")
    finally:
        if conn:
            conn.close()

# Entry point of the script
if __name__ == "__main__":
    try:
        # Ensure the data directory exists
        if not os.path.exists('data'):
            os.makedirs('data')

        # Initialize the database
        initialize_database()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
