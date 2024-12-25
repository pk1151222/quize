from utils.pdf_generator import generate_pdf
from telegram import Document

def generate_report(update, context):
    user_id = update.message.from_user.id
    pdf_path = generate_pdf(user_id)

    if pdf_path:
        with open(pdf_path, "rb") as pdf_file:
            update.message.reply_document(pdf_file, filename="Quiz_Report.pdf")
    else:
        update.message.reply_text("Failed to generate the report.")
