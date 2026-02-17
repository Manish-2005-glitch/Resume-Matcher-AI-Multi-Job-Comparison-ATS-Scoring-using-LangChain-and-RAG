from engine.skill_extractor import extract_skills


def ats_score(resume, job_desc):

    resume_skills = set(
        extract_skills(resume)
    )

    jd_skills = set(
        extract_skills(job_desc)
    )

    if len(jd_skills) == 0:

        return 0, []

    matched = resume_skills.intersection(
        jd_skills
    )

    missing = jd_skills - resume_skills

    score = (
        len(matched) / len(jd_skills)
    ) * 100

    return round(score, 2), list(missing)
