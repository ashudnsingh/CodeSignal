def reverseOnDiagonals(m):
    for i in range(int(len(m)/2)):
        m[i][i],m[-i-1][-i-1]=m[-i-1][-i-1],m[i][i]
        m[i][-i-1],m[-i-1][i]=m[-i-1][i],m[i][-i-1]
    return m
