def runnersMeetings(p, s):
    if len(set(p))!=len(set(s)): return -1
    v = (p[1]-p[0])/(s[0]-s[1])
    m = [v*j+p[i] for i,j in enumerate(s)]
    return len(p)-len(set(m))+1
