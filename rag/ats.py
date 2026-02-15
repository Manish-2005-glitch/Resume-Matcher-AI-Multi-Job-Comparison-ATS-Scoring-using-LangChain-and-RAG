def ats_score(resume, job_desc):
    
    resume_words = set(resume.lower().split())
    
    jd_words = set(job_desc.lower().split())
    
    matched = resume_words.intersection(jd_words)
    
    score = (len(matched) / len(jd_words)) * 100
    
    missing = jd_words - resume_words
    
    return round(score,2), list(missing)[:20]