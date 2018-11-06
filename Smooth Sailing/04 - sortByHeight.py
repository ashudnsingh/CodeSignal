def sortByHeight(a):
    b = sorted([x for x in a if x != -1])
    print (b)
    j = 0
    for i in range(a.__len__()) :
        if a[i] != -1 :
            a[i] = b[j]
            j += 1
            
    return a
