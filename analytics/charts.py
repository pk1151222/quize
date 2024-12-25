import matplotlib.pyplot as plt
from database.db import connect_db
import os

def generate_performance_chart(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT subject, SUM(score) FROM quizzes WHERE user_id = ? GROUP BY subject", (user_id,))
    data = cursor.fetchall()
    conn.close()

    if not data:
        return None

    subjects, scores = zip(*data)
    plt.bar(subjects, scores, color='skyblue')
    plt.title("Performance by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Scores")
    plt.tight_layout()

    chart_path = f"data/reports/chart_{user_id}.png"
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

    return chart_path

def send_chart(update, context):
    user_id = update.message.from_user.id
    chart_path = generate_performance_chart(user_id)

    if chart_path:
        with open(chart_path, "rb") as chart_file:
            update.message.reply_photo(chart_file, caption="Your Performance Chart")
    else:
        update.message.reply_text("No data available to generate chart.")
