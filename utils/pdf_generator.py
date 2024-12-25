from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from database.db import connect_db
import os

def generate_pdf(user_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username, score FROM users WHERE user_id = ?", (user_id,))
    user_data = cursor.fetchone()
    conn.close()

    if not user_data:
        return None

    username, score = user_data
    pdf_path = f"data/reports/report_{user_id}.pdf"

    os.makedirs(os.path.dirname(pdf_path), exist_ok=True)

    c = canvas.Canvas(pdf_path, pagesize=letter)
    c.drawString(100, 750, f"Quiz Report for {username or 'Anonymous'}")
    c.drawString(100, 730, f"Total Score: {score}")
    c.save()

    return pdf_path
