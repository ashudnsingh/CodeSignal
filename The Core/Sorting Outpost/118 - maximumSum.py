def maximumSum(a, q):
    l = [i for l,r in q for i in range(l,r+1)]
    s = sorted([l.count(i) for i in set(l)])[::-1]
    return sum([i*j for i,j in zip(s,sorted(a)[::-1])])
