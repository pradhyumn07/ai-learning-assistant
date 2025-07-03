import pdfplumber

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages[:5]:  # Limit to first 5 pages
            text += page.extract_text() + "\n"
    return text
