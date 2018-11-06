def lineEncoding(s):
    cCount  = 0
    resStr  = ''
    prevChr = ''
    for c in list(s) :
        if prevChr == '' :
            cCount  = 1
        elif prevChr == c :
            cCount += 1
        else :
            if cCount == 1 :
                resStr += prevChr
            else :
                resStr += str(cCount) + prevChr
            cCount  = 1
        prevChr = c
    if cCount == 1 :
        resStr += prevChr
    else :
        resStr += str(cCount) + prevChr
    return resStr
