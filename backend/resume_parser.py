import pdfplumber
import spacy
import re
import json

# Load the small English model for spaCy
nlp = spacy.load("en_core_web_sm")

SKILLS_DB = ['python', 'java', 'sql', 'c++', 'machine learning', 'excel', 'pandas', 'keras']


def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def clean_text(text):
    return ' '.join(text.split())


def extract_email(text):
    match = re.search(r'\S+@\S+', text)
    return match.group() if match else None


def extract_phone(text):
    match = re.search(r'\b\d{10}\b', text)
    return match.group() if match else None

def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None




#def extract_skills(text):
  #  text = text.lower()  # convert everything to lowercase for matching
   # return [skill for skill in SKILLS_DB if skill in text]



def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if re.search(r'\b' + re.escape(skill) + r'\b', text)]



def parse_resume(pdf_path):
    text = extract_text_from_pdf(pdf_path)     # Step 1: Extract raw text from PDF
    text = clean_text(text)                    # Step 2: Clean up whitespace and formatting

    return {
        "name": extract_name(text),            # Step 3: Get person's name
        "email": extract_email(text),          # Step 4: Get email address
        "phone": extract_phone(text),          # Step 5: Get phone number
        "skills": extract_skills(text),        # Step 6: Get skills list
        "raw_text": text[:500]                 # Step 7: Show a preview (first 500 characters only)
    }




#if __name__ == "__main__":
   # resume_data = parse_resume("data/resumes/sample_resume.pdf")  # 👈 replace filename if needed
   # print(json.dumps(resume_data, indent=2))  # 👈 pretty-prints the result
