def chessBishopDream(boardSize, pos, Dir, k):
    [x,y] = boardSize
    orgPos = list(pos)
    initDir = list(Dir)
    for n in range(x*y*4):
        orgDir = list(Dir)

        if pos[0]+Dir[0]<0:
            Dir[0] = 1
        elif pos[0]+Dir[0]>=x:
            Dir[0] = -1
        if pos[1]+Dir[1]<0:
            Dir[1] = 1
        elif pos[1]+Dir[1]>=y:
            Dir[1] = -1

        temp = [(i+j)/2 for (i,j) in zip(orgDir,Dir)]
        pos = [i+j for (i,j) in zip(pos,temp)]
        if n==(k-1):
            break
        if pos == orgPos and Dir==initDir:

            break
    
    if n!=(k-1):
        for m in range(k%(n+1)):
            orgDir = list(Dir)

            if pos[0]+Dir[0]<0:
                Dir[0] = 1
            elif pos[0]+Dir[0]>=x:
                Dir[0] = -1
            if pos[1]+Dir[1]<0:
                Dir[1] = 1
            elif pos[1]+Dir[1]>=y:
                Dir[1] = -1
        
            temp = [(i+j)/2 for (i,j) in zip(orgDir,Dir)]
            pos = [i+j for (i,j) in zip(pos,temp)]
            
    return pos
