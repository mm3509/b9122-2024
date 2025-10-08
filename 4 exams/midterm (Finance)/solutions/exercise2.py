def get_grade(uni, grades):
    """
    Find the student's UNI in a dictionary, and returns its grade.
    
    >>> grades = {"mm3509": {"gsb": "MMorin26", "grade": 42}}
    >>> get_grade("mm3509", grades)
    42
    >>> get_grade("MMorin26", grades)
    42
    """
    if not isinstance(uni, str):
        raise ValueError("UNI must be a string")

    if uni == "":
        return None

    uni = uni.lower()
    if uni in grades:
        return grades[uni]["grade"]

    for uni_inner_loop in grades:
        person = grades[uni_inner_loop]
        if "gsb" in person and person["gsb"].lower() == uni:
            return grades[uni_inner_loop]["grade"]

    return None

