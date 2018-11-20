from collections import defaultdict
def digitJumping(grid, start, finish):
    row, col = len(grid), len(grid[0])
    nearest = defaultdict(lambda : float('inf'))
    nearest_index = {}
    distance = lambda x1,y1,x2,y2 : abs(x1 - x2) + abs(y1 - y2)
    for i in range(row):
        for j in range(col):
            num = grid[i][j]
            d = distance(i,j, *finish)
            if  d < nearest[num]:
                nearest_index[num] = (i,j)
                nearest[num] = d           
    queue = [start + [0]]
    visited = numpy.zeros((row,col))
    m,n = start
    visited[m,n] = 1
    while queue:
        i, j, dis = queue.pop(0)
        if [i,j] == finish : return dis 
        m,n = nearest_index[grid[i][j]]
        if m != i or n !=j :
            queue.append([m,n, dis + 1])
        for x,y in (0,1), (1,0), (-1,0), (0,-1):
            if 0 <= x + i < row and 0 <= y + j < col :
                    queue.append((x + i, y +j , dis + 1))
