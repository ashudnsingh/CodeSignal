def jumpingJimmy(t, j):
    res = 0
    for h in t :
        if h <= j :
            res += h
        else :
            break
    return res 
