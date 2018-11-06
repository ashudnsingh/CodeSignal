def combs(c1, c2):
    c1,l = "-"*(len(c2)-2)+c1+"-"*(len(c2)-2),[]
    for i in range(len(c1)-(len(c2)-1)):
        b,t = "-"*i+c2+"-"*(len(c1)-len(c2)-i),[]
        for j,k in zip(c1,b):
            if not (j=="-" and k=="-"): t.append([j,k])
        if all(j!=["*","*"] for j in t): l.append(t)
    return min(len(i) for i in l) if len(l)>0 else len(c1)-1
