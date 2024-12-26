from database.db import get_db_connection

def get_quiz_questions():
    conn = get_db_connection()
    cursor = conn.execute("SELECT * FROM questions")
    questions = cursor.fetchall()
    conn.close()
    return questions

def save_user_quiz(user_id, quiz_data):
    conn = get_db_connection()
    conn.execute(
        "INSERT INTO user_quizzes (user_id, title, data) VALUES (?, ?, ?)",
        (user_id, quiz_data["title"], str(quiz_data))
    )
    conn.commit()
    conn.close()
