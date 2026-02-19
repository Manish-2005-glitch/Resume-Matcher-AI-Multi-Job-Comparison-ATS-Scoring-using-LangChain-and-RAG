from langchain_text_splitters import CharacterTextSplitter
from rag.vector_store import create_vector_store
from rag.prompts import prompt
from rag.ats import ats_score
from rag.llm import get_llm
import shutil
import os


def run_rag(resume: str, job_desc: str):

    if os.path.exists("chroma_db"):
        shutil.rmtree("chroma_db")

    splitter = CharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separator="\n"
    )

    chunks = splitter.split_text(resume)

    db = create_vector_store(chunks)

    retriever = db.as_retriever(
        search_kwargs={"k": 5}
    )

    docs = retriever.invoke(job_desc)

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    ats_score_value, missing_skills = ats_score(
        resume,
        job_desc
    )

    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke({
        "resume": resume,
        "job_desc": job_desc,
        "context": context,
        "ats_score": ats_score_value,
        "missing_skills": ", ".join(missing_skills)
    })


    return {

        "ats_score": ats_score_value,

        "missing_skills": missing_skills,

        "retrieved_chunks": len(docs),

        "feedback": response.content

    }
