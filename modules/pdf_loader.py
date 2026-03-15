import PyPDF2

def load_pdf(file) -> str:
    try:
        reader = PyPDF2.PdfReader(file)
        text = ""

        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

        return text

    except Exception as e:
        return f"Error reading PDF: {str(e)}"