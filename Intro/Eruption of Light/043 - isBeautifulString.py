def isBeautifulString(inputString):
    chars  = [chr(x) for x in range (ord('a'),ord('z')+1)]
    inpStr = list ( inputString )
    for c in inpStr :
        print ( c )
        if c == 'a' :
            pass
        elif inpStr.count(c) > inpStr.count(chr(ord(c)-1)) :
            print (chr(ord(c)-1))
            print ( inpStr.count(c) )
            print ( inpStr.count(chr(ord(c)-1)) )
            return False
    return True
