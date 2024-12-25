import sqlite3

def connect_db():
    conn = sqlite3.connect('data/db.sqlite3')
    return conn

def setup_db():
    conn = connect_db()
    cursor = conn.cursor()
    
    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        username TEXT,
        language TEXT DEFAULT 'en',
        score INTEGER DEFAULT 0
    )
    """)

    # Quizzes Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS quizzes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        options TEXT,
        answer INTEGER,
        difficulty TEXT,
        subject TEXT
    )
    """)
    
    conn.commit()
    conn.close()
