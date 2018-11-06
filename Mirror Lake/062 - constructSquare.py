def constructSquare(s):
    sq = [i**2 for i in range(int(math.sqrt(int("9"*len(s)))),math.ceil(math.sqrt(int("1"+"0"*(len(s)-1))))-1,-1)]
    for i in sq:
        if sorted([s.count(j) for j in set(s)]) == sorted([str(i).count(j) for j in set(str(i))]): return i
    return -1
