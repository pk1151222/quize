async def feedback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    feedback_text = update.message.text

    # Save feedback to the database or a log file
    conn = get_db_connection()
    conn.execute("INSERT INTO feedback (user_id, feedback) VALUES (?, ?)", (user_id, feedback_text))
    conn.commit()
    conn.close()

    await update.message.reply_text("Thank you for your feedback!")
