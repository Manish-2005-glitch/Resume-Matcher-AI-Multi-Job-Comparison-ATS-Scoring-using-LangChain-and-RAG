import streamlit as st
import requests


BACKEND_URL = "http://localhost:8000/analyze"


st.title("ResumeAI — Resume Matcher")


file = st.file_uploader(
    "Upload Resume",
    type=["pdf","docx"]
)

job1 = st.text_area("Job Description 1")
job2 = st.text_area("Job Description 2")
job3 = st.text_area("Job Description 3")


if st.button("Analyze Resume"):

    if file and job1:

        files = {

            "file": file.getvalue()
        }

        data = {

            "job1": job1,
            "job2": job2,
            "job3": job3
        }


        response = requests.post(

            BACKEND_URL,

            files={
                "file": (
                    file.name,
                    file.getvalue()
                )
            },

            data=data

        )


        result = response.json()


        st.subheader("Skills")

        st.write(result["skills"])


        st.subheader("Job Rankings")

        st.write(result["rankings"])


        st.metric(
            "ATS Score",
            f"{result['ats_score']}%"
        )


        st.subheader("Missing Skills")

        st.write(result["missing_skills"])


        st.subheader("AI Feedback")

        st.write(result["feedback"])
