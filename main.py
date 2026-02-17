from fastapi import FastAPI, UploadFile, File, File, Form
from fastapi.middleware.cors import CORSMiddleware

from rag.parser import parse_docx, parse_pdf
from rag.chain import run_rag

from engine.skill_extractor import extract_skills
from engine.job_matcher import rank_jobs

app = FastAPI(title="Resume Review RAG System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from io import BytesIO

@app.post("/analyze")
async def analyze_resume(

    file: UploadFile = File(...),
    job1: str = Form(...),
    job2: str = Form(None),
    job3: str = Form(None)

):

    content = await file.read()

    file_obj = BytesIO(content)

    if file.filename.endswith(".pdf"):
        resume = parse_pdf(file_obj)

    elif file.filename.endswith(".docx"):
        resume = parse_docx(file_obj)

    else:
        return {"error": "Unsupported file format"}


    skills = extract_skills(resume)


    job_list = [job1, job2, job3]
    job_list = [j for j in job_list if j]

    rankings = rank_jobs(resume, job_list)


    best_job = rankings[0]["job_description"]


    rag_result = run_rag(resume, best_job)


    return {

        "skills": skills,

        "rankings": rankings,

        "ats_score": rag_result["ats_score"],

        "missing_skills": rag_result["missing_skills"],

        "feedback": rag_result["feedback"]

    }
