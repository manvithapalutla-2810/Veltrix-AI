skills_database = [
    "python",
    "java",
    "sql",
    "c",
    "c++",
    "javascript",
    "html",
    "css",
    "react",
    "node",
    "streamlit",
    "tensorflow",
    "keras",
    "pytorch",
    "machine learning",
    "deep learning",
    "data analytics",
    "power bi",
    "tableau",
    "excel",
    "git",
    "github",
    "mysql",
    "mongodb",
    "aws",
    "docker",
    "linux",
    "communication",
    "problem solving"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_database:
        if skill in text:
            found_skills.append(skill)

    return list(set(found_skills))