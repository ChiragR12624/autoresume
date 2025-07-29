from resume_parser import parse_resume
from job_parser import parse_jd
import json

# ✅ Skill Weights
SKILL_WEIGHTS = {
    "python": 5,
    "sql": 3,
    "aws": 2,
    "pandas": 2,
    "scikit-learn": 2,
    "gcp": 1,
    "machine learning": 2,
    "excel": 1,
}

# ✅ Learning Resources for Missing Skills
SKILL_RESOURCES = {
    "aws": "https://www.coursera.org/learn/aws-fundamentals",
    "scikit-learn": "https://scikit-learn.org/stable/tutorial/basic/tutorial.html",
    "sql": "https://www.codecademy.com/learn/learn-sql",
    "pandas": "https://pandas.pydata.org/docs/getting_started/index.html",
    "gcp": "https://www.cloudskillsboost.google/",
    "machine learning": "https://www.coursera.org/learn/machine-learning",
    "excel": "https://exceljet.net/",
    "python": "https://docs.python.org/3/tutorial/"
}

def match(resume_path, jd_path):
    try:

        resume_data = parse_resume(resume_path)
        jd_data = parse_jd(jd_path)

        resume_skills = set(resume_data["skills"])
        jd_skills = set(jd_data["skills_required"])

        matched_skills = resume_skills.intersection(jd_skills)
        missing_skills = jd_skills - resume_skills

    # ✅ Weighted score calculation
        total_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in jd_skills)
        matched_weight = sum(SKILL_WEIGHTS.get(skill, 1) for skill in matched_skills)
        score = matched_weight / total_weight if total_weight else 0

    # ✅ Suggest resources for missing skills
        suggested_courses = {
            skill: SKILL_RESOURCES.get(skill)
            for skill in missing_skills
            if skill in SKILL_RESOURCES
        }

        return {
            "match_score_percent": round(score * 100, 2),
            "matched_skills": list(matched_skills),
            "missing_skills": list(missing_skills),
            "suggested_courses": suggested_courses,
            "resume_skills": list(resume_skills),
            "jd_skills": list(jd_skills),
        }
    except Exception as e:
        return {"error": str(e)}
# ✅ Save to JSON
if __name__ == "__main__":
    result = match("../data/resumes/sample_resume.pdf", "../data/jobs/sample_jd.txt")

    with open("../data/match_output.json", "w") as f:
        json.dump(result, f, indent=2)

    # Optional: Also print to console
    from pprint import pprint
    pprint(result)



