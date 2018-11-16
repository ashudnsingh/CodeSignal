def livingOnTheRoads(roadRegister):
    c = sorted({tuple(sorted([i, j])) for i in range(len(roadRegister)) for j in range(len(roadRegister)) if roadRegister[i][j]})
    return [[i!=j and bool(set(i)&set(j)) for j in c] for i in c]
