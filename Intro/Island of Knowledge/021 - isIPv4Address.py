def isIPv4Address(inputString):
    sString = inputString.split(".")
    if sString.__len__() != 4:
        return False
    for p in sString:
        if p.__len__() == 0 or not p.isdigit() or int(p) > 255 or int(p) < 0 :
            return False
    return True
