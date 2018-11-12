def snakeGame(game_board, commands):
    
    def find_body(x, y):
        for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            inside_board = (
                i in range(len(game_board)) 
                and j in range(len(game_board[0]))
            )
            if inside_board and game_board[i][j] == '*' and (i, j) not in body:
                body.append((i, j))
                find_body(i, j)
                return
    
    def move(dx, dy, body):
        x, y = body[0]
        head = (x + dx, y + dy)
        inside_board = (
            head[0] in range(len(game_board)) 
            and head[1] in range(len(game_board[0]))
        )        
        if not inside_board or head in body[:-1]:
            return False
        else:
            body[:] = [head] + body[:-1]
            return True
        
    def end_game_board(dir_=None):
        for i, row in enumerate(game_board):
            for j, e in enumerate(row):
                if (i, j) in body:
                    if dir_ is not None:
                        if (i, j) == body[0]:
                            game_board[i][j] = {0: "<", 1: "^", 2: ">", 3: "v"}[dir_]
                        else:
                            game_board[i][j] = "*"
                    else:
                        game_board[i][j] = "X"
                else:
                    game_board[i][j] = "."
        
        return game_board
    
    body = [
        (i, j)
        for i, row in enumerate(game_board) 
        for j, e in enumerate(row) 
        if e in "<v^>"
    ]
    x, y = body[0]
    directions = ((0, -1), (-1, 0), (0, 1), (1, 0))
    dir_ = {"<": 0, "^": 1, ">": 2, "v": 3}[game_board[x][y]]
    dx, dy = directions[dir_]
    prev = (x - dx, y - dy)
    body.append(prev)
    find_body(*prev)
    
    for c in commands:
        if c == "F" and not move(dx, dy, body):
            return end_game_board()
            
        if c == "R":
            dir_ = (dir_ + 1) % 4
            dx, dy = directions[dir_]
            
        if c == "L":
            dir_ = (dir_ - 1) % 4
            dx, dy = directions[dir_]
        
    return end_game_board(dir_)
