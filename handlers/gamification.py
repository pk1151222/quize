def reward_badge(update, context):
    user_id = update.message.from_user.id
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT score FROM users WHERE user_id = ?", (user_id,))
    score = cursor.fetchone()[0]

    if score >= 50:
        badge = "🏅 Gold Badge"
    elif score >= 30:
        badge = "🥈 Silver Badge"
    else:
        badge = "🥉 Bronze Badge"

    update.message.reply_text(f"Congratulations! You've earned a {badge}")
