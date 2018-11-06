def digitDegree(n):
    degree = 0
    sumNum = 0

    if n < 10 :
        return 0

    degree += 1
    
    for x in list(str(n)) :
        sumNum += int(x)

    if int(sumNum/10) > 0 :
        degree += digitDegree(sumNum)
    else :
        return degree
    
    return degree
