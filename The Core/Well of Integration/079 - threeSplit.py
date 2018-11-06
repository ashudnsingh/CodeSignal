def threeSplit(a):
    l = [sum(a[:i+1]) for i in range(len(a))]
    b = l[-1]//3
    r = [i for i in range(len(a)-2) if l[i]==b]
    return sum(l[i+1:-1].count(2*b) for i in r)
