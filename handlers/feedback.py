async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    feedback_text = update.message.text

    # Save feedback to the database or a log file
    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (user_id, feedback) VALUES (?, ?)", (user_id, feedback_text))
    conn.commit()
    conn.close()

    await update.message.reply_text("Thank you for your feedback!")

def initialize_database():
    conn = get_db_connection()
    conn.executescript('''
    CREATE TABLE IF NOT EXISTS feedback (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        feedback TEXT
    );
    ''')
    conn.commit()
    conn.close()
