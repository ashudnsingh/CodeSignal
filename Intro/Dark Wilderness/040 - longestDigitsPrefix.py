def longestDigitsPrefix(inputString):
    largestNum = []
    digits     = []
    for c in list(inputString) :
        if c.isdigit() :
            digits.append(c)
        else :
            if digits.__len__() > 0 and digits.__len__() > largestNum.__len__() :
                largestNum = digits
            digits = []
            break
    if digits.__len__() > largestNum.__len__() :
        largestNum = digits
    return "".join(largestNum)
