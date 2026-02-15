import fitz
import docx

def parse_pdf(file):
    
    text = ""
    
    pdf= fitz.open(stream = file.read(), filetype = "pdf")
    
    for page in pdf:
        
        text += page.get_text()
        
    return text

def parse_docx(file):
    
    doc = docx.Document(file)
    
    text = "\n".join(p.text for p in doc.paragraphs)
    
    return text