def messageFromBinaryCode(code):
    return "".join([chr(x) for x in [ int("".join([c for c in code] [i:i+8]),2) for i in range(0,code.__len__(),8) ] ])
