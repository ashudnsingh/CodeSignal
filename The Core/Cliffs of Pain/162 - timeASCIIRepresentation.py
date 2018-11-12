def timeASCIIRepresentation(dtime):
    D = ["***.***", "*..*..*", "*.***.*", "*.**.**", ".***.*.", "**.*.**", "**.****", "*.*..*.", "*******", "****.**"]
    d = [D.index("".join(dtime[j][i+k] for j, k in [[0, 1], [4, 0], [4, 2], [8, 1], [12, 0], [12, 2], [16, 1]])) for i in [1, 5, 10, 14]]
    return [["*" if abs(math.sqrt((i-8)**2+(j-8)**2)-8.5) < math.sqrt(0.5) or math.sqrt((i-8)**2+(j-8)**2) < 8.5 and any([(j-8)*math.sin(a*2*math.pi)+(8-i)*math.cos(a*2*math.pi) >= 0 and abs((j-8)*math.cos(a*2*math.pi)-(8-i)*math.sin(a*2*math.pi)) < math.sqrt(0.5)-1e-9 for a in [(10*d[0]+d[1]+(10*d[2]+d[3])/60)/12, (10*d[2]+d[3])/60]]) else "." for j in range(17)] for i in range(17)]
