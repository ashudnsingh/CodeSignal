def deleteDigit(n):
    n      = list(str(n))
    maxNum = 0
    for i in range(0,n.__len__()) :
        n1 = int("".join([n[x] for x in range(0,n.__len__()) if x != i ]))
        if n1 > maxNum :
            maxNum = n1
    return maxNum
