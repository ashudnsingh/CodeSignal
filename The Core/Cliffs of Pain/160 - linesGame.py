def linesGame(field, clicks, newBalls, newBallsCoordinates):
    field = numpy.array(field)
    global point
    point = index = 0
    def bfs(x,y, x1,y1):
        seen = {(x, y)}
        queue = [(x, y)]
        while queue:
            x,y = queue.pop(0)
            for i, j in (0, 1), (1, 0), (0, -1), (-1, 0):
                if 0 <= x + i < 9 and 0 <= y + j < 9:
                    if field[x+i,y+j] == '.' and (x+i,y+j) not in seen:
                        seen.add((x+i,y+j))
                        queue.append((x+i,y+j))
        return (x1,y1) in seen
    def formline(x,y,m,n, color):
        seen = {(x, y)}
        for i,j in [(m, n), (-m, -n)]:
            k = 1
            while 1:
                p, q = x + i * k, y + j * k
                if 0 <= p < 9 and 0 <= q < 9 and field[p,q] == color:
                    seen.add((p,q))
                else:
                    break
                k += 1
        return len(seen) >= 5, seen
    def disappear(x, y, eat = 1):
        global point
        found = total = line = 0
        remove, tmp = set(), set()
        for m,n in [(0, -1), (-1, -1), (-1, 0), (-1, 1)]:
            isline, seen = formline(x,y,m,n, field[x,y])
            if isline:
                line += 1
                total += len(seen)
                remove |= seen
                tmp.add(tuple(sorted(seen)))
                found = 1
        if found:
            if eat:
                point += line + total - 1
                for i,j in remove:
                    field[i,j] = '.'
                return 1 
            return tmp
        return 0         
    while index < len(clicks) - 1:
        one, two = tuple(clicks[index]), tuple(clicks[index+1])
        if field[one] != '.' and field[two] == '.' and bfs(*one, * two):
                field[two] = field[one]
                field[one] = '.'
                if not disappear(*two):
                    consider = set()
                    for _ in range(3):
                        x, y = newBallsCoordinates.pop(0)
                        consider.add((x, y))
                        field[x,y] = newBalls.pop(0)
                    line, check = set(), 0
                    for x,y in consider:
                        tmp = disappear(x,y,0)
                        if tmp:
                            check = 1
                            line |= tmp
                    if check:
                        point += len(line) + sum(map(len, line)) - 1
                        line = {j for i in line for j in i }
                        for i,j in line:  
                            field[i,j] = '.'
                index += 2
        else:
            index += 1
    return point
