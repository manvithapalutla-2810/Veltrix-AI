from utils.skill_extractor import extract_skills


def calculate_ats_score(job_description, resume):

    jd_skills = extract_skills(job_description)
    resume_skills = extract_skills(resume)

    matched = list(set(jd_skills) & set(resume_skills))
    missing = list(set(jd_skills) - set(resume_skills))

    if len(jd_skills) == 0:
        score = 0
    else:
        score = round((len(matched) / len(jd_skills)) * 100)

    return score, matched, missing