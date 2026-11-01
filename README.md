# AutoResume – Intelligent Resume and Job Description Matcher

<p align="center">
  <b>An NLP-powered platform for intelligent resume analysis, job-description matching, and personalized skill development.</b>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?logo=python" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?logo=streamlit" />
  <img src="https://img.shields.io/badge/NLP-Scikit--learn-orange" />
  <img src="https://img.shields.io/badge/SpaCy-NLP-green" />
  <img src="https://img.shields.io/badge/Status-Developed-success" />
</p>

---

## 1. Project Overview

The recruitment process increasingly relies on automated systems to evaluate resumes against job requirements. However, candidates often struggle to identify how well their qualifications align with specific job descriptions and which skills they need to develop to improve their employability.

**AutoResume** is an intelligent resume analysis and job-description matching platform that leverages Natural Language Processing (NLP) and machine learning techniques to evaluate candidate profiles against job requirements.

The system extracts relevant information from uploaded resumes and job descriptions, identifies overlapping skills, calculates a matching score, highlights missing competencies, and recommends relevant courses to support targeted skill development.

By combining automated document processing, NLP-based skill analysis, and interactive visualizations, AutoResume aims to make resume evaluation more informative and actionable.

## 2. Key Features

- **Resume Upload and Parsing:** Extract relevant information and skills from PDF resumes.
- **Job Description Analysis:** Process pasted or uploaded job descriptions to identify required competencies.
- **Intelligent Skill Matching:** Compare candidate skills against job requirements using NLP-based techniques.
- **Resume–Job Matching Score:** Generate a quantitative indication of alignment between a resume and a job description.
- **Skill Gap Identification:** Highlight missing or unmatched skills that may require further development.
- **Personalized Course Recommendations:** Suggest learning resources based on identified skill gaps.
- **Interactive Visualizations:** Present skill comparisons and matching insights using Matplotlib and Plotly.
- **PDF Feedback Export:** Generate downloadable reports containing resume analysis and improvement suggestions.

## 3. System Architecture

AutoResume follows a modular client-server architecture consisting of a FastAPI backend and a Streamlit-based user interface.

```text
              USER INPUT
                  |
          +-------+-------+
          |               |
       Resume PDF     Job Description
          |               |
          v               v
     Resume Parser     JD Parser
          |               |
          v               v
     Skill Extraction and Text Processing
                  |
                  v
          NLP-Based Skill Matching
                  |
                  v
          Matching Score Calculation
                  |
          +-------+-------+
          |               |
          v               v
     Missing Skills   Matched Skills
          |
          v
   Course Recommendations
          |
          v
    Visualization and Analysis
          |
          v
       PDF Feedback Report
```

## 4. Methodology

### 4.1 Resume Parsing

The system accepts resumes in PDF format and extracts textual information using PDFMiner.six.

The extracted content is processed to identify relevant candidate skills and information required for subsequent analysis.

### 4.2 Job Description Processing

Users can paste or upload a job description. The system processes the provided text to identify the skills and competencies expected for the position.

### 4.3 NLP-Based Skill Matching

The extracted resume information and job requirements are analyzed using NLP techniques.

The matching component identifies:

- Skills present in both documents.
- Skills required by the job description but missing from the resume.
- Overall alignment between the candidate profile and job requirements.

Scikit-learn and spaCy support the text-processing and machine-learning components.

### 4.4 Skill Gap Analysis

The system compares identified candidate skills against the requirements of the target job description.

Unmatched requirements are highlighted to help candidates understand areas where additional learning or experience may be beneficial.

### 4.5 Course Recommendation

Based on the identified skill gaps, the recommendation component suggests relevant courses to help candidates strengthen their knowledge and improve their alignment with job requirements.

### 4.6 Visualization and Report Generation

The platform uses Matplotlib and Plotly to present skill-matching insights visually.

Users can also export the generated feedback as a PDF report using FPDF.

## 5. Technology Stack

| Component | Technologies |
|---|---|
| Programming Language | Python |
| Backend Framework | FastAPI |
| Frontend Framework | Streamlit |
| Natural Language Processing | spaCy |
| Machine Learning | Scikit-learn |
| PDF Text Extraction | PDFMiner.six |
| Data Processing | Python |
| Visualization | Matplotlib, Plotly |
| PDF Report Generation | FPDF |
| API Communication | Python-Multipart |

## 6. Repository Structure

```text
autoresume/
│
├── SystemDesign/          # System design documentation
│
├── backend/               # FastAPI backend implementation
│   ├── api.py
│   ├── requirements.txt
│   └── start.sh
│
├── data/                  # Project data and supporting resources
│
├── frontend/              # Frontend components
│
├── streamlit_ui/          # Streamlit application
│   ├── app.py
│   ├── resume_parser.py
│   ├── jd_parser.py
│   ├── skill_matcher.py
│   ├── visualizer.py
│   ├── recommender.py
│   └── utils/
│
├── README.md
└── .gitignore
```

## 7. Installation and Execution

### Prerequisites

- Python 3.10 or later
- pip
- Git

### Step 1: Clone the Repository

```bash
git clone https://github.com/ChiragR12624/autoresume.git

cd autoresume
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**macOS / Linux**

```bash
source venv/bin/activate
```

**Windows**

```bash
venv\Scripts\activate
```

### Step 3: Install Backend Dependencies

```bash
pip install -r backend/requirements.txt
```

### Step 4: Install Frontend Dependencies

```bash
pip install -r streamlit_ui/requirements.txt
```

### Step 5: Run the Backend

```bash
cd backend
uvicorn api:app --reload
```

### Step 6: Launch the Streamlit Interface

Open another terminal, activate the virtual environment, and execute:

```bash
cd streamlit_ui
streamlit run app.py
```

*Note: These commands assume the dependency files and entry points are present at the paths shown in the repository. If your deployment configuration uses different commands, follow the corresponding configuration.*

## 8. Deployment

The project has been deployed using Render with independently hosted application components:

- **FastAPI Backend:** Handles backend processing and API requests.
- **Streamlit Frontend:** Provides the interactive user interface.

This separation enables the frontend and backend components to be maintained and deployed independently.

## 9. Applications

AutoResume can support several career-development activities:

- Evaluating resume alignment with specific job opportunities.
- Identifying missing technical skills.
- Understanding skill gaps before applying for positions.
- Discovering relevant learning resources.
- Generating structured resume feedback.

The platform is intended to assist candidates in evaluating their profiles rather than replace human recruitment decisions.

## 10. Future Enhancements

Potential improvements include:

- Integrating transformer-based language models for more context-aware skill extraction.
- Exploring semantic similarity techniques for improved resume–job matching.
- Incorporating generative AI for personalized resume improvement suggestions.
- Supporting additional document formats.
- Expanding course recommendations using personalized learning profiles.
- Introducing explainable matching to clarify how individual skills influence the overall score.
- Extending job-description analysis to additional employment platforms.

## 11. Author

**Chirag R. Gowda**

Computer Science and Engineering

Research Interests: Machine Learning, Natural Language Processing, Generative AI, and Intelligent Systems.

GitHub: ChiragR12624

---

*AutoResume demonstrates the application of NLP and machine learning to practical career-development challenges through intelligent document analysis and skill-gap identification.*
