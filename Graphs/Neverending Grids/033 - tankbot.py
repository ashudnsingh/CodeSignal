def tankbot(forest):
    row, col, max = len(forest), len(forest[0]), 0
    def valid(x1,y1,x2,y2, size, passed, d = None):  
        f = passed[x1:y1, x2:y2].flatten()
        return all(f) and any(f == 1) and 0 <= x1 <= row - size and 0 <= x2 <= col - size
     
    #simple bfs 
    def bfs(size):
        queue = [[0, size, 0, size]]
        passed = numpy.array(forest, 'i8')
        if not valid(0,size,0,size, size, passed):  return 0
        passed[0:size, 0:size] = -1 
        while queue:
            x1, y1, x2, y2 = queue.pop(0)
            if x1 == row - size and x2 == col - size:
                return 1
            for i,j in (-1, 0), (1, 0), (0, -1), (0, 1):
                x3, y3, x4, y4 = x1 + i, y1 + i, x2 + j, y2 + j
                
                if valid(x3,y3,x4,y4,size, passed, 1):
                    passed[x3:y3,x4:y4] = -1                        #set passed parts = -1
                    queue.append((x3,y3,x4,y4))
        return 0 
    while bfs(max + 1) :  
        max += 1 
    return max
