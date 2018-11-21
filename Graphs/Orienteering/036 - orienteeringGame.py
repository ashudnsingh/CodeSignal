import heapq
def orienteeringGame(board):
    b = [(board[0][0],0,0)]
    time = {(0,0):board[0][0]}
    
    end = (len(board)-1, len(board[0])-1)
    while b:
        cur = heapq.heappop(b)
        x,y = (cur[1], cur[2])
        d = cur[0]
        
        for nx, ny in [(x+1,y), (x-1, y), (x,y+1), (x, y-1)]:
            if nx >= 0 and nx <= end[0] and ny >=0 and ny <= end[1]:
                new_d = d + board[nx][ny]
                if new_d < time.get((nx,ny), float('inf')):
                    time[(nx,ny)] = new_d
                    heapq.heappush(b, (new_d, nx, ny))
    return time[end] - board[end[0]][end[1]]
