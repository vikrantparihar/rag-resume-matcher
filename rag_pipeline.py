def rag_pipeline(resume_text):

    jobs = {
        "AI Engineer": ["Python", "Machine Learning", "Deep Learning", "NLP"],
        "Data Scientist": ["Python", "Statistics", "SQL", "ML"],
        "Backend Developer": ["Node.js", "APIs", "Databases"],
        "Frontend Developer": ["React", "HTML", "CSS", "JavaScript"]
    }

    results = []

    for role, skills in jobs.items():
        matched = [skill for skill in skills if skill.lower() in resume_text.lower()]
        missing = [skill for skill in skills if skill.lower() not in resume_text.lower()]

        results.append(f"{role}:\nMatched Skills: {matched}\nMissing Skills: {missing}\n")

    return "\n".join(results)