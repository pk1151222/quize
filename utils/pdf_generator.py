from fpdf import FPDF

def generate_pdf_report(user_id, scores):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="Quiz Report", ln=True, align='C')

    for subject, score in scores.items():
        pdf.cell(200, 10, txt=f"{subject}: {score}", ln=True, align='L')

    report_path = f"data/reports/{user_id}_report.pdf"
    pdf.output(report_path)
    return report_path
