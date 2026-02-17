import re

SKILL_DB = [

"python","java","c++","sql",

"machine learning","deep learning",
"nlp","computer vision",

"pytorch","tensorflow","scikit-learn",

"langchain","rag","llm","transformers",

"aws","gcp","azure",

"fastapi","flask",

"docker","kubernetes","git",

"pandas","numpy",

"postgresql","mongodb",

"react","nodejs"
]


def extract_skills(text):

    text = text.lower()

    skills = []

    for skill in SKILL_DB:

        if re.search(
            r"\b" + re.escape(skill) + r"\b",
            text
        ):
            skills.append(skill)

    return skills
