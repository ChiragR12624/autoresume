#from fastapi import FastAPI, UploadFile, File
#from fastapi.middleware.cors import CORSMiddleware
#from resume_parser import parse_resume
#from job_parser import parse_jd
#from matcher import match
#import shutil
#from pydantic import BaseModel
#import os

#app = FastAPI()

# ✅ Enable CORS
#app.add_middleware(
#   CORSMiddleware,
 #   allow_origins=["*"],  # Later replace "*" with ["http://127.0.0.1:5500"]
 #   allow_credentials=True,
  #  allow_methods=["*"],
   # allow_headers=["*"],
#)


#@app.get("/")
#def root():
 #   return {"message": "Welcome to AutoResume API!"}

#@app.post("/upload-resume/")
#async def upload_resume(file: UploadFile = File(...)):
    #os.makedirs("temp_resumes", exist_ok=True)
    #file_path = f"temp_resumes/{file.filename}"
 #   save_path = f"temp_resumes/{file.filename}"
    #with open(file_path, "wb") as f:
  #  with open(save_path, "wb") as f:
   #     f.write(await file.read())
    #return {"path": file_path}
    #return {"path": save_path}
    #os.makedirs("temp_resumes", exist_ok=True)
    
    #    f.write(await file.read())
    # return parse_resume(file_path)

 #   file_location = f"resume_files/{file.filename}"
 #   os.makedirs("resume_files", exist_ok=True)
 #   with open(file_location, "wb") as buffer:
 #       shutil.copyfileobj(file.file, buffer)
#    return {"path": file_location}

    
#@app.post("/upload-jd/")
#async def upload_jd(file: UploadFile = File(...)):
 #   #file_path = f"temp_jobs/{file.filename}"
 #   save_path = f"temp_jobs/{file.filename}"
    #os.makedirs("temp_jobs", exist_ok=True)
    #file_path = f"temp_jobs/{file.filename}"
  #  with open(save_path, "wb") as f:
   #     f.write(await file.read())
   # return {"path": save_path}
    #os.makedirs("temp_jobs", exist_ok=True)
    #with open(file_path, "wb") as f:
     #   f.write(await file.read())
   # return parse_jd(file_path)
   # file_location = f"jd_files/{file.filename}"
  #  os.makedirs("jd_files", exist_ok=True)
  #  with open(file_location, "wb") as buffer:
  #      shutil.copyfileobj(file.file, buffer)
   # return {"path": file_location}

#class MatchRequest(BaseModel):
 #   resume_path: str
  #  jd_path: str   

#@app.post("/match/")
#sync def match_resume_and_jd(resume_path: str, jd_path: str):
    #return match(resume_path, jd_path)
 #   return {
  #      "match_score": 85,
   #     "matched_skills": ["Python", "FastAPI"],
    #    "missing_skills": ["Docker"]
    #}

#@app.post("/match/")
#async def match_resume_and_jd(data: MatchRequest):
 #   resume_path = data.resume_path
  #  jd_path = data.jd_path

    # ✅ Call your actual matching logic
   # result = match(resume_path, jd_path)

   # return result



#from fastapi import FastAPI, UploadFile, File, Query
#from fastapi.middleware.cors import CORSMiddleware
#import shutil
#import os

##app = FastAPI()

# Enable CORS for development (change origins in production)
#app.add_middleware(
#    CORSMiddleware,
#    allow_origins=["*"],  
#    allow_credentials=True,
#    allow_methods=["*"],
#    allow_headers=["*"],
#)

#@app.get("/")
#def root():
#    return {"message": "Welcome to AutoResume API!"}

#@app.post("/upload-resume/")
#async def upload_resume(file: UploadFile = File(...)):
#    file_location = f"resume_files/{file.filename}"
#    os.makedirs("resume_files", exist_ok=True)
#    with open(file_location, "wb") as buffer:
#        shutil.copyfileobj(file.file, buffer)
#    return {"path": file_location}

#@app.post("/upload-jd/")
#async def upload_jd(file: UploadFile = File(...)):
#    file_location = f"jd_files/{file.filename}"
#    os.makedirs("jd_files", exist_ok=True)
#    with open(file_location, "wb") as buffer:
#        shutil.copyfileobj(file.file, buffer)
#    return {"path": file_location}

#@app.get("/match/")
#async def match_resume_and_jd(
#    resume_path: str = Query(...),
#    jd_path: str = Query(...)
#):
#    # Dummy match logic for demonstration
#    # Replace this with your real matching logic from matcher.py
 #   result = {
 #       "match_score": 85,
 #       "matched_skills": ["Python", "FastAPI"],
 #       "missing_skills": ["Docker"]
 #   }
 #   return result






from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import fitz  # PyMuPDF
import spacy

spacy.cli.download("en_core_web_sm")
nlp = spacy.load("en_core_web_sm")

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AutoResume API is live!"}

# Enable CORS (adjust origins for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load spaCy model once at startup
nlp = spacy.load("en_core_web_sm")

UPLOAD_DIR_RESUME = "temp_resumes"
UPLOAD_DIR_JD = "temp_jobs"
os.makedirs(UPLOAD_DIR_RESUME, exist_ok=True)
os.makedirs(UPLOAD_DIR_JD, exist_ok=True)

# Suggested courses for missing skills
COURSE_SUGGESTIONS = {
    "pandas": "https://www.kaggle.com/learn/pandas",
    "numpy": "https://www.kaggle.com/learn/numpy",
    "tensorflow": "https://www.tensorflow.org/tutorials",
    "scikit": "https://scikit-learn.org/stable/tutorial/",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "deep learning": "https://www.deeplearning.ai/",
    "docker": "https://www.docker.com/101-tutorial",
    "gcp": "https://cloud.google.com/training",
    "rest": "https://restfulapi.net/",
    "aws": "https://aws.amazon.com/training/",
    "flask": "https://flask.palletsprojects.com/en/2.3.x/tutorial/",
    "django": "https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django",
}

class MatchRequest(BaseModel):
    resume_path: str
    jd_path: str = None
    jd_text: str = None

def extract_text_from_pdf(file_path: str) -> str:
    """Extract all text from PDF file using PyMuPDF."""
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading PDF: {e}")

def extract_skills(text: str) -> set:
    """Extract a set of known skill keywords from the input text."""
    skill_keywords = set([
        "python", "java", "c++", "sql", "machine learning", "data science",
        "deep learning", "nlp", "pandas", "numpy", "flask", "django",
        "gcp", "aws", "docker", "kubernetes", "linux", "git", "rest",
        "react", "node", "mongodb", "scikit", "tensorflow"
    ])
    doc = nlp(text.lower())
    tokens = set(token.text for token in doc if not token.is_stop and not token.is_punct)
    return tokens & skill_keywords

@app.post("/upload-resume/")
async def upload_resume(file: UploadFile = File(...)):
    """Save uploaded resume PDF to disk."""
    file_location = os.path.join(UPLOAD_DIR_RESUME, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"path": file_location}

@app.post("/upload-jd/")
async def upload_jd(file: UploadFile = File(...)):
    """Save uploaded job description TXT to disk."""
    file_location = os.path.join(UPLOAD_DIR_JD, file.filename)
    with open(file_location, "wb") as f:
        f.write(await file.read())
    return {"path": file_location}

@app.post("/match/")
async def match_resume_and_jd(data: MatchRequest):
    """Match resume and job description skills, return match score and suggestions."""
    # Extract text from resume PDF
    resume_text = extract_text_from_pdf(data.resume_path)

    # Get JD text either from path or pasted text
    if data.jd_text:
        jd_text = data.jd_text
    elif data.jd_path:
        try:
            with open(data.jd_path, "r", encoding="utf-8") as f:
                jd_text = f.read()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading JD file: {e}")
    else:
        raise HTTPException(status_code=400, detail="Either jd_path or jd_text must be provided.")

    # Extract skills
    resume_skills = extract_skills(resume_text)
    jd_skills = extract_skills(jd_text)

    # Calculate matched and missing skills
    matched_skills = sorted(resume_skills & jd_skills)
    missing_skills = sorted(jd_skills - resume_skills)

    # Calculate match score safely
    match_score = round((len(matched_skills) / len(jd_skills)) * 100, 2) if jd_skills else 0.0

    # Suggested courses for missing skills
    suggested_courses = {
        skill: COURSE_SUGGESTIONS[skill]
        for skill in missing_skills
        if skill in COURSE_SUGGESTIONS
    }

    return {
        "match_score": match_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "suggested_courses": suggested_courses,
    }
