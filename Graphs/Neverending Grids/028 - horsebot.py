def horsebot(n, m):
    ret = 0
    for i in range(1, max(n,m)):
        for j in range(i, max(n,m)):
            dx = [i, -i, i, -i, j, j, -j, -j]
            dy = [j, j, -j, -j, i, -i, i, -i]
            seen = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                x, y = stack.pop()
                for z in range(8):
                    newx = x + dx[z]
                    if not 0 <= newx < n:
                        continue
                    newy = y + dy[z]
                    if not 0 <= newy < m:
                        continue
                    if newx == n-1 and newy == m-1:
                        # End
                        ret += 1
                        break
                    if (newx, newy) not in seen:
                        seen.add((newx, newy))
                        stack.append((newx, newy))
                else:
                    continue
                break
    return ret
