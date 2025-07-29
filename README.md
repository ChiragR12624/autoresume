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
├── backend/                          # FastAPI backend logic
│   ├── api.py                        # Main FastAPI app
│   ├── requirements.txt              # Backend dependencies
│   └── start.sh                      # Startup script for deployment
│
├── streamlit_ui/                    # Streamlit frontend interface
│   ├── app.py                        # Main Streamlit app
│   ├── resume_parser.py              # Resume parsing logic
│   ├── jd_parser.py                  # JD parsing logic
│   ├── skill_matcher.py              # Matching and scoring
│   ├── visualizer.py                 # Matplotlib/Plotly charts
│   ├── recommender.py                # Course recommendations
│   ├── requirements.txt              # Frontend dependencies
│   └── utils/                        # Helper functions, shared logic
│
├── Dockerfile.backend                # Dockerfile for backend
├── Dockerfile.frontend               # Dockerfile for frontend
├── docker-compose.yml                # For multi-container setup
│
├── .gitignore                        # Git ignored files
├── README.md                         # Project overview and documentation



---

## 🛡️ Privacy Notice

AutoResume runs locally or securely on cloud platforms. Uploaded resumes and job descriptions are **not stored** or shared.

---

## 📌 Author

Chirag Gowda


