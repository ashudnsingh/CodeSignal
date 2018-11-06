import itertools, collections
def crosswordFormation(words):
    ans = 0
    for p in itertools.permutations(words):
        M = collections.defaultdict(int)
        a,b,c,d = p
        for i in range(2, min(a.__len__(),b.__len__())):
            for p in range(a.__len__() - i):
                for q in range(b.__len__() - i):
                    M[a[p],a[p+i],b[q],b[q+i]] += 1
        for i in range(2, min(c.__len__(),d.__len__())):
            for p in range(c.__len__() - i):
                for q in range(d.__len__() - i):
                    ans += M[c[p],d[q],c[p+i],d[q+i]]
    return ans
