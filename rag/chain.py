from langchain_text_splitters import CharacterTextSplitter
from vector_store import create_vector_store
from prompts import prompt
from ats import ats_score
from llm import get_llm


llm = get_llm()

def run_rag(resume, job_desc):
    
    splitter = CharacterTextSplitter(
        chunk_size = 500,
        chunk_overlap = 50
    )
    
    chunks = splitter.split_text(resume)
    
    db = create_vector_store(chunks)
    
    retriever = db.as_retriever()
    
    docs = retriever.invoke(job_desc)
    
    context = "\n".join(
        [doc.page_coontent for doc in docs]
    )
    
    score, missing = ats_score(resume, job_desc)
    
    chain = prompt | llm
    
    response = chain.invoke({

        "resume": resume,
        "job_desc": job_desc,
        "context": context
    })

    return {

        "ats_score": score,
        "missing_skills": missing,
        "feedback": response
    }