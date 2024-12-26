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

async def reward_badge(user_id, achievement):
    conn = get_db_connection()
    conn.execute("INSERT INTO badges (user_id, badge) VALUES (?, ?)", (user_id, achievement))
    conn.commit()
    conn.close()

async def check_rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    conn = get_db_connection()
    cursor = conn.execute("SELECT badge FROM badges WHERE user_id = ?", (user_id,))
    badges = cursor.fetchall()
    conn.close()

    if badges:
        message = "🎖️ Your Badges:\n" + "\n".join([badge["badge"] for badge in badges])
    else:
        message = "You don't have any badges yet. Keep playing!"
    
    await update.message.reply_text(message)
