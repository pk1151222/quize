from telegram import Update
from telegram.ext import ContextTypes
from database.db import get_db_connection

async def reward_badge(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Provide badge based on user's score (bilingual)."""
    user_id = update.effective_user.id
    language_code = update.effective_user.language_code  # Get user's language code

    # Determine language
    if language_code == 'hi':  # Hindi
        messages = {
            "no_score": "आपने अभी तक कोई स्कोर अर्जित नहीं किया है। बैज प्राप्त करने के लिए क्विज़ खेलें!",
            "duplicate_badge": "आप पहले ही यह बैज अर्जित कर चुके हैं!",
            "rewarded": "बधाई हो! आपने {badge} अर्जित किया है।",
            "error": "कुछ गड़बड़ हो गई, कृपया बाद में पुनः प्रयास करें।"
        }
    else:  # Default to English
        messages = {
            "no_score": "You haven't earned any score yet. Play the quiz to earn a badge!",
            "duplicate_badge": "You've already earned this badge!",
            "rewarded": "Congratulations! You've earned the {badge} badge.",
            "error": "Something went wrong, please try again later."
        }

    try:
        # Get score
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT score FROM users WHERE user_id = ?", (user_id,))
            result = cursor.fetchone()

            if not result:
                await update.message.reply_text(messages["no_score"])
                return

            score = result[0]

            # Determine badge
            if score >= 50:
                badge = "🏅 Gold Badge"
            elif score >= 30:
                badge = "🥈 Silver Badge"
            else:
                badge = "🥉 Bronze Badge"

            # Check for duplicate badge
            cursor.execute("SELECT 1 FROM badges WHERE user_id = ? AND badge = ?", (user_id, badge))
            if cursor.fetchone():
                await update.message.reply_text(messages["duplicate_badge"])
                return

            # Add badge
            cursor.execute("INSERT INTO badges (user_id, badge) VALUES (?, ?)", (user_id, badge))
            conn.commit()

        await update.message.reply_text(messages["rewarded"].format(badge=badge))
    except Exception as e:
        await update.message.reply_text(messages["error"])

async def check_rewards(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Show the user's badges (bilingual)."""
    user_id = update.effective_user.id
    language_code = update.effective_user.language_code  # Get user's language code

    # Determine language
    if language_code == 'hi':  # Hindi
        messages = {
            "no_badges": "आपके पास अभी तक कोई बैज नहीं है। खेलते रहें!",
            "your_badges": "🎖️ आपके बैज:\n{badges}"
        }
    else:  # Default to English
        messages = {
            "no_badges": "You don't have any badges yet. Keep playing!",
            "your_badges": "🎖️ Your badges:\n{badges}"
        }

    try:
        # Get badges
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT badge FROM badges WHERE user_id = ?", (user_id,))
            badges = cursor.fetchall()

        if badges:
            badge_list = "\n".join([row[0] for row in badges])
            message = messages["your_badges"].format(badges=badge_list)
        else:
            message = messages["no_badges"]

        await update.message.reply_text(message)
    except Exception as e:
        await update.message.reply_text(messages["no_badges"])
