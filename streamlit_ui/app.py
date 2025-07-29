import streamlit as st
import requests
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from fpdf import FPDF

st.set_page_config(page_title="AutoResume Matcher", page_icon="🧠")
st.title("🧠 AutoResume Matcher")

# Initialize session state variables
if "resume_path" not in st.session_state:
    st.session_state.resume_path = None
if "jd_path" not in st.session_state:
    st.session_state.jd_path = None
if "jd_text" not in st.session_state:
    st.session_state.jd_text = None

# --- Resume Upload Section ---
st.header("Step 1: Upload Your Resume (PDF)")
resume_file = st.file_uploader("📄 Upload Resume (PDF)", type=["pdf"], key="resume_uploader")
if resume_file:
    try:
        res = requests.post(
            "http://127.0.0.1:8000/upload-resume/",
            files={"file": (resume_file.name, resume_file, "application/pdf")},
            timeout=15,
        )
        res.raise_for_status()
        st.session_state.resume_path = res.json().get("path")
        st.success(f"✅ Resume uploaded: {resume_file.name}")
    except Exception as e:
        st.error(f"Failed to upload resume: {e}")
        st.session_state.resume_path = None

if st.button("🔄 Upload New Resume"):
    st.session_state.resume_path = None
    st.session_state.jd_path = None
    st.session_state.jd_text = None
    #st.experimental_rerun()
    st.success("Please refresh the page to continue.")
    
# --- Job Description Section ---
st.header("Step 2: Provide Job Description")

jd_input_mode = st.radio("Choose JD Input Method:", options=["Upload JD File (TXT)", "Paste JD Text"])

if jd_input_mode == "Upload JD File (TXT)":
    jd_file = st.file_uploader("📝 Upload Job Description (TXT)", type=["txt"], key="jd_file_uploader")
    if jd_file:
        try:
            res = requests.post(
                "http://127.0.0.1:8000/upload-jd/",
                files={"file": (jd_file.name, jd_file, "text/plain")},
                timeout=15,
            )
            res.raise_for_status()
            st.session_state.jd_path = res.json().get("path")
            st.session_state.jd_text = None
            st.success(f"✅ Job Description uploaded: {jd_file.name}")
        except Exception as e:
            st.error(f"Failed to upload JD: {e}")
            st.session_state.jd_path = None
            st.session_state.jd_text = None

elif jd_input_mode == "Paste JD Text":
    jd_text = st.text_area("📝 Paste your Job Description here", height=200)
    if jd_text.strip():
        st.session_state.jd_text = jd_text
        st.session_state.jd_path = None
    else:
        st.session_state.jd_text = None

if st.button("🔄 Clear JD Input"):
    st.session_state.jd_path = None
    st.session_state.jd_text = None
    st.experimental_rerun()

# --- Matching Section ---
match_ready = st.session_state.resume_path and (st.session_state.jd_path or st.session_state.jd_text)

if st.button("🚀 Match Resume & JD", disabled=not match_ready):
    if not match_ready:
        st.warning("Please upload resume and provide job description before matching.")
    else:
        with st.spinner("Matching..."):
            try:
                # If JD text pasted, send text directly, else send jd_path
                payload = {"resume_path": st.session_state.resume_path}
                if st.session_state.jd_path:
                    payload["jd_path"] = st.session_state.jd_path
                else:
                    payload["jd_text"] = st.session_state.jd_text

                match_res = requests.post(
                    "http://127.0.0.1:8000/match/",
                    json=payload,
                    timeout=30,
                )
                match_res.raise_for_status()
                data = match_res.json()

                # Display Results
                st.subheader("🎯 Match Results")
                score = data.get("match_score", 0)
                st.markdown(f"**Skill Match Score:** `{score}%`")

                matched_skills = data.get("matched_skills", [])
                missing_skills = data.get("missing_skills", [])
                courses = data.get("suggested_courses", {})

                st.markdown("✅ **Matched Skills**:")
                st.markdown(", ".join(f"`{skill}`" for skill in matched_skills) or "_None_")

                st.markdown("❌ **Missing Skills**:")
                st.markdown(", ".join(f"`{skill}`" for skill in missing_skills) or "_None_")

                # Pie Chart - Skill Match Score Breakdown
                fig1, ax1 = plt.subplots()
                ax1.pie(
                    [score, 100 - score],
                    labels=["Matched", "Not Matched"],
                    autopct="%1.1f%%",
                    colors=["#4CAF50", "#FF6F61"],
                )
                ax1.set_title("Skill Match Score Breakdown")
                st.pyplot(fig1)

                # Bar Chart - Matched vs Missing Skills
                fig2 = go.Figure(
                    data=[
                        go.Bar(name="Matched Skills", x=matched_skills, y=[1] * len(matched_skills), marker_color="green"),
                        go.Bar(name="Missing Skills", x=missing_skills, y=[1] * len(missing_skills), marker_color="red"),
                    ]
                )
                fig2.update_layout(barmode="stack", title="Matched vs Missing Skills")
                st.plotly_chart(fig2, use_container_width=True)

                # Suggested Courses
                if courses:
                    st.markdown("📚 **Suggested Courses to Improve Missing Skills:**")
                    for skill, url in courses.items():
                        st.markdown(f"- [{skill.title()}]({url})")
                else:
                    st.info("🎉 Great! No course suggestions needed.")

                # PDF Export Button
                if st.button("📄 Export Feedback as PDF"):
                    pdf = FPDF()
                    pdf.add_page()
                    pdf.set_font("Arial", size=12)
                    pdf.cell(0, 10, "AutoResume Match Feedback", ln=True, align="C")
                    pdf.ln(10)
                    pdf.cell(0, 10, f"Skill Match Score: {score}%", ln=True)
                    pdf.ln(5)
                    pdf.cell(0, 10, "Matched Skills:", ln=True)
                    for skill in matched_skills:
                        pdf.cell(0, 10, f"- {skill}", ln=True)
                    pdf.ln(5)
                    pdf.cell(0, 10, "Missing Skills:", ln=True)
                    for skill in missing_skills:
                        pdf.cell(0, 10, f"- {skill}", ln=True)
                    if courses:
                        pdf.ln(5)
                        pdf.cell(0, 10, "Suggested Courses:", ln=True)
                        for skill, url in courses.items():
                            pdf.multi_cell(0, 10, f"- {skill.title()}: {url}")

                    pdf_bytes = pdf.output(dest="S").encode("latin1")

                    st.download_button(
                        label="📥 Download Feedback PDF",
                        data=pdf_bytes,
                        file_name="autoresume_feedback.pdf",
                        mime="application/pdf",
                    )

            except Exception as e:
                st.error(f"❌ Error occurred during matching: {e}")
else:
    if not match_ready:
        st.info("⬆️ Please upload Resume and provide Job Description to enable matching.")
