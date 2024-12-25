from database.db import connect_db

def create_quiz(update, context):
    args = context.args
    if len(args) < 4:
        update.message.reply_text("Usage: /create_quiz <question> | <option1,option2,...> | <correct_option_index> | <subject>")
        return
    
    question, options, correct_option, subject = args[0], args[1], args[2], args[3]
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO quizzes (question, options, answer, subject) VALUES (?, ?, ?, ?)
    """, (question, options, correct_option, subject))
    conn.commit()
    conn.close()
    
    update.message.reply_text("Quiz created successfully!")
