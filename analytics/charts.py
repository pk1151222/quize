import matplotlib.pyplot as plt
import os

def generate_performance_chart(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT subject, score FROM quizzes WHERE user_id = ?", (user_id,))
    data = cursor.fetchall()
    conn.close()

    if not data:
        return None

    subjects, scores = zip(*data)
    plt.bar(subjects, scores)
    plt.title("Performance by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Scores")

    chart_path = f"data/reports/chart_{user_id}.png"
    os.makedirs(os.path.dirname(chart_path), exist_ok=True)
    plt.savefig(chart_path)
    plt.close()

    return chart_path
