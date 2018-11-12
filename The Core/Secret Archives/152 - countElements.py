def countElements(inputString):
    return len(re.findall(r'(\"[^\"]*\"|\d+|true|false)', inputString))
