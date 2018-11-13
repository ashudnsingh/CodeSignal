def financialCrisis(roadRegister):
    r = roadRegister
    s = []
    for d in range(len(r)):
        n = [i for i in range(d)]+[i for i in range(d+1,len(r))]
        s += [[[r[i][j] for i in n] for j in n]]
    return s
