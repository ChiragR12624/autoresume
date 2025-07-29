import re


SKILLS_DB = ['python', 'java', 'sql', 'c++', 'machine learning', 'excel', 'pandas', 'keras', 'scikit-learn', 'aws', 'gcp']

def extract_skills_from_jd(text):
    text = text.lower()
    return [skill for skill in SKILLS_DB if skill in text]

def extract_experience(text):
     
    match = re.search(r'(\d+)[\+–\-]?\s*(years|yrs)', text.lower())
    return match.group(1) if match else None

def parse_jd(file_path):
    with open(file_path, 'r') as file:
        jd_text = file.read()

    return {
        "skills_required": extract_skills_from_jd(jd_text),
        "min_experience": extract_experience(jd_text),
        "raw_text": jd_text[:500]  
    }


if __name__ == "__main__":
    parsed = parse_jd("../data/jobs/sample_jd.txt")
    from pprint import pprint
    pprint(parsed)
