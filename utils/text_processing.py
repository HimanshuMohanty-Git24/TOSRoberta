import PyPDF2
import spacy
import re

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

def split_into_clauses(text):
    # Preprocess the text
    text = re.sub(r'\s+', ' ', text)  # Remove extra whitespace
    text = re.sub(r'\n+', '\n', text)  # Remove extra newlines
    
    # Use spaCy to parse the text
    doc = nlp(text)
    
    clauses = []
    current_clause = []
    
    for sent in doc.sents:
        current_clause.append(sent.text)
        
        # Check if this sentence ends a clause
        if re.search(r'\d+\.|\([a-z]\)|\([iv]+\)', sent.text) or len(' '.join(current_clause)) > 200:
            clauses.append(' '.join(current_clause))
            current_clause = []
    
    # Add any remaining text as the last clause
    if current_clause:
        clauses.append(' '.join(current_clause))
    
    # Post-process clauses
    cleaned_clauses = []
    for clause in clauses:
        # Remove leading/trailing whitespace and numbers
        clause = re.sub(r'^\s*\d+\.?\s*', '', clause.strip())
        if clause:
            cleaned_clauses.append(clause)
    
    return cleaned_clauses