#from resume_parser import extract_text_from_pdf
#pdf_path = "../data/resumes/sample_resume.pdf"
#text = extract_text_from_pdf(pdf_path)
#print("🔍 Extracted Resume Text:\n")
#print(text[:1000])  # print only first 1000 characters


#from resume_parser import extract_text_from_pdf, clean_text
#pdf_path = "../data/resumes/sample_resume.pdf"
#raw_text = extract_text_from_pdf(pdf_path)
#cleaned = clean_text(raw_text)
#print("✅ Cleaned Resume Text:\n")
#print(cleaned[:1000])  # Show first 1000 characters



#from resume_parser import extract_text_from_pdf, clean_text, extract_email, extract_phone, extract_name, extract_skills
#pdf_path = "../data/resumes/sample_resume.pdf"
#raw_text = extract_text_from_pdf(pdf_path)
#leaned = clean_text(raw_text)
#print("🧹 Cleaned Text:\n", cleaned[:500])  # First 500 chars
#print("\n📧 Email:", extract_email(cleaned))
#print("📱 Phone:", extract_phone(cleaned))
#print("👤 Name:", extract_name(cleaned))
#print("🧠 Skills:", extract_skills(cleaned))




from resume_parser import parse_resume
pdf_path = "../data/resumes/sample_resume.pdf"
parsed_data = parse_resume(pdf_path)
print(parsed_data)
