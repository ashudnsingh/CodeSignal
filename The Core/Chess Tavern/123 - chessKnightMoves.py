def chessKnightMoves(cell):
    moves=[-2,-1,1,2]
    res=0

    for i in moves:
        for j in moves:
            if (abs(i) != abs(j) and ord('a') <= ord(cell[0]) + i <= ord('h') and 1 <= int(cell[1]) + j <= 8):
                res+=1
    return res
