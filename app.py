import streamlit as st
import requests
from dotenv import load_dotenv
import os

load_dotenv()

BACKEND_URL = os.getenv("BACKEND_URL")


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
                    file.getvalue(),
                    file.type
                )
            },
            data={
                "job1": job1,
                "job2": job2,
                "job3": job3
            }
        )

        st.write("Status Code:", response.status_code)

        try:
            result = response.json()
        except Exception:
            st.error("Invalid response from backend")
            st.text(response.text)
            st.stop()

        if response.status_code != 200:
            st.error("Backend returned error")
            st.json(result)
            st.stop()

        required_keys = ["skills", "rankings", "ats_score", "missing_skills", "feedback"]

        for key in required_keys:
            if key not in result:
                st.error(f"Missing key in response: {key}")
                st.json(result)
                st.stop()

        st.subheader("Extracted Skills")
        st.write(result["skills"])

        st.subheader("Job Rankings")
        st.write(result["rankings"])

        st.subheader("ATS Score")
        st.metric("Score", f"{result['ats_score']}%")

        st.subheader("Missing Skills")
        st.write(result["missing_skills"])

        st.subheader("AI Feedback")
        st.write(result["feedback"])

