import numpy as np
from rag.embeddings import get_embeddings

embedder = get_embeddings()

def cosine_similarity(a,b):
    
    a = np.array(a)
    b = np.array(b)
    
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

def rank_jobs(resume, job_list):
    
    resume_emb = embedder.embed_query(resume)
    
    results = []
    
    for job in job_list:
        
        job_emb = embedder.embed_query(job)
        
        score = cosine_similarity(resume_emb, job_emb)
        
        results.append({
            "job_description": job,
            "score": round(score*100, 2)
        })
        
    results.sort(
        key=lambda x:x["score"],
        reverse=True
    )

    return results