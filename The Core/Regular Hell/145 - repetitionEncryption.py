def repetitionEncryption(letter):
    pattern =  r"([a-zA-Z]+)[^a-zA-Z]+\1(?![a-zA-Z])"
    regex = re.compile(pattern,re.IGNORECASE)
    return len(re.findall(regex, letter))
