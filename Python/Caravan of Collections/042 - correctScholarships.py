def correctScholarships(bestStudents, scholarships, allStudents):
    return set(bestStudents).issubset(set(scholarships)) and set(scholarships).issubset(set(allStudents)) and not set(allStudents).issubset(set(scholarships))
