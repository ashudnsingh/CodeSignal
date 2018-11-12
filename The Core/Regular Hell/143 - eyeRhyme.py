def eyeRhyme(pairOfLines):
    pattern = ".*(...)\t.*(...)"
    match = re.match(pattern, pairOfLines)
    return match.group(1) == match.group(2)
