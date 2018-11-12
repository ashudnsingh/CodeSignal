def onboard(x,n,m):
    if 1<=x[0]<=n and 1<=x[1]<=m:
        return True
    return False

def RookBishop(cell,n,m):
    move = 0
    moves = [[1,2],[2,1],[-1,-2],[-2,-1],[-1,2],[-2,1],[1,-2],[2,-1]]
    for x in moves:
        temp = [i+j for (i,j) in zip(cell,x)]
        if onboard(temp,n,m):
            i = x[0]
            j = x[1]
            if onboard([cell[0]+i,cell[1]+i],n,m):
                move+=1
            if onboard([cell[0]+j,cell[1]+j],n,m):
                move+=1
            if onboard([cell[0]+i,cell[1]-i],n,m):
                move+=1
            if onboard([cell[0]-j,cell[1]+j],n,m):
                move+=1
    return move

def chessTriangle(n, m):
    if n==1 or m==1:
        return 0
    if n<3 and m<3:
        return 0
    output = 0
    for x in range(1,n+1):
        for y in range(1,m+1):
            output += RookBishop([x,y],n,m)
    return output*2
