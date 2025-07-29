# AutoResume - Intelligent Resume and JD Matcher

AutoResume is a smart tool that compares resumes with job descriptions using advanced Natural Language Processing (NLP). It highlights matching skills, missing ones, and recommends courses to upskill.

---

## 🚀 Features

- 📄 Upload Resume (PDF)
- 📋 Paste or Upload Job Description
- ✅ Skill Matching Score
- ❌ Missing Skills Identification
- 🎓 Course Recommendations
- 📊 Skill Visualizations (Matplotlib & Plotly)
- 📥 Export Feedback as PDF

---

## 🧠 Tech Stack

### Backend (FastAPI)
- FastAPI
- PDFMiner.six
- Scikit-learn
- SpaCy
- Python-Multipart

### Frontend (Streamlit)
- Streamlit
- FPDF
- Matplotlib / Plotly

---

## 🌐 Deployment

Hosted on **Render** with:
- ⚙️ FastAPI Backend deployed independently
- 🖥️ Streamlit Frontend served separately

---

## 📁 Project Structure

autoresume/

│
├── backend/                        
│   ├── api.py                        
│   ├── requirements.txt              
│   └── start.sh                      
│
├── streamlit_ui/                    
│   ├── app.py                        
│   ├── resume_parser.py              
│   ├── jd_parser.py                  
│   ├── skill_matcher.py              
│   ├── visualizer.py                 
│   ├── recommender.py                
│   ├── requirements.txt              
│   └── utils/                        
│
├── .gitignore                       
├── README.md                         



---

## 🛡️ Privacy Notice

AutoResume runs locally or securely on cloud platforms. Uploaded resumes and job descriptions are **not stored** or shared.

---

## 📌 Author

Chirag Gowda


