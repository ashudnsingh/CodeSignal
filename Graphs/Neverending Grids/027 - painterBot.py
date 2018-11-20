def painterBot(canvas, operations, d):
    row, col = len(canvas), len(canvas[0])
    new = numpy.array(canvas)
    def bfs(canvas, p, q, color):
        visited = numpy.zeros((row, col))
        visited[p,q] = 1
        new[p,q] = color
        queue = [[p, q]]
        while queue:
            x, y = queue.pop(0)
            for i,j in (0,1),(1,0),(0,-1),(-1,0):
                if 0 <= x + i < row and 0 <= y + j < col:
                    if not visited[x + i, y + j]:
                       
                        if abs(canvas[x + i][y + j] - canvas[p][q]) <= d:
                            visited[x + i][y + j] = 1 
                            new[x + i, y + j] = color 
                            queue.append((x + i, y + j))
        return new
    for k in operations:
        canvas = bfs(canvas, *k).copy()
    return new
