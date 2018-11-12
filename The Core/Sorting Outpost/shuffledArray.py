def shuffledArray(s):
    p = [i for i in s]
    for x in s :
        p.remove(x)
        print ( p )
        if x == sum(p) :
            s.remove(x)
            break
        p = [i for i in s]
    return sorted(s)
