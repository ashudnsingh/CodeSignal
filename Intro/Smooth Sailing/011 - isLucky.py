def isLucky(n):
    num   = list(str(n))
    sLen  = num.__len__()
    fHalf = [int(num[x]) for x in range(0,int(sLen/2))]
    sHalf = [int(num[x]) for x in range(int(sLen/2),sLen)]
    print ( sLen )
    print ( fHalf )
    print ( sHalf )
    if sum(fHalf) == sum (sHalf) :
        return True
    else :
        return False
