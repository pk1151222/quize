from database.db import connect_db
from telegram import ParseMode

def view_scores(update, context):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT username, score FROM users ORDER BY score DESC LIMIT 10
    """)
    top_scorers = cursor.fetchall()
    conn.close()

    if not top_scorers:
        update.message.reply_text("No scores available yet!")
        return

    leaderboard = "🏆 <b>Leaderboard</b> 🏆\n"
    for i, (username, score) in enumerate(top_scorers, start=1):
        leaderboard += f"{i}. {username or 'Anonymous'} - {score} points\n"

    update.message.reply_text(leaderboard, parse_mode=ParseMode.HTML)



async def display_leaderboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    conn = get_db_connection()
    cursor = conn.execute('''
        SELECT user_id, SUM(score) as total_score 
        FROM scores 
        GROUP BY user_id 
        ORDER BY total_score DESC 
        LIMIT 10
    ''')
    leaderboard = cursor.fetchall()
    conn.close()

    message = "🏆 Leaderboard:\n\n"
    for rank, row in enumerate(leaderboard, start=1):
        message += f"{rank}. User {row['user_id']}: {row['total_score']} points\n"

    await update.message.reply_text(message)
