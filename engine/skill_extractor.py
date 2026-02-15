import re

SKILL_DB = [

"python","java","c++","sql",
"machine learning","deep learning",
"nlp","computer vision",
"pytorch","tensorflow","keras",

"langchain","rag","llm",
"transformers",

"aws","gcp","azure",
"docker","kubernetes",

"fastapi","flask","streamlit",

"pandas","numpy","scikit-learn",

"mongodb","postgresql",

"git","linux",

"data science",
"data analysis",

"react","nodejs"
]

def extract_skill(resume):
    resume = resume.lower()
    skills= []
    
    for skill in SKILL_DB:
        pattern = r"\b" + re.escape(skill) + r"\b"
        
        if re.search(pattern, resume):
            skills.append(skill)
            
    return skills