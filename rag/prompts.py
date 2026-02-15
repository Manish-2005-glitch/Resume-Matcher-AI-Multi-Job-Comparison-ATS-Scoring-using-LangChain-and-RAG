from langchain_core.prompts import PromptTemplate

template = """
You are a senior FAANG recruiter.

Analyze the resume aginst job description.

Job Description:
{job_desc}

Resume Context:
{context}

Resume:
{resume}

Provide detailed:

1. Strengths
2. Weaknesses
3. Missing skills
4. Improvements
5. Final verdict

"""

prompt = PromptTemplate(
    template=template,
    input_variables=["job_desc", "context", "resume"]
)