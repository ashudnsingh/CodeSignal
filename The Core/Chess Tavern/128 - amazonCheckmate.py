def amazonCheckmate(king, amazon):
    king = [int(king[1]) - 1, ord(king[0]) - ord("a")]
    amazon = [int(amazon[1]) - 1, ord(amazon[0]) - ord("a")]
    board = [[3] * 8 for _ in range(8)]
    result = [0] * 4
    
    def near_king(x, y):
        return abs(king[0] - x) < 2 and abs(king[1] - y) < 2
    
    def covered(x, y):
        horizontal = amazon[0] == king[0] == x and (y - king[1]) * (king[1] - amazon[1]) > 0
        vertical = amazon[1] == king[1] == y and (x - king[0]) * (king[0] - amazon[0]) > 0
        diagonal = (
            (amazon[0] - amazon[1] == king[0] - king[1] == x - y
             or sum(amazon) == sum(king) == x + y)
            and (x - king[0]) * (king[0] - amazon[0]) > 0
        )
        return horizontal or vertical or diagonal
      
    def under_attack(x, y):
        on_diagonal = amazon[1] - amazon[0] == y - x or sum(amazon) == x + y
        on_straight = amazon[0] == x or amazon[1] == y
        on_rhombus = abs(amazon[0] - x) + abs(amazon[1] - y) == 3
        return not covered(x, y) and (on_diagonal or on_straight or on_rhombus)
    
    def safe_spot_num(x, y):
        spot_num = 0
        
        for k in range(i - 1, i + 2):
            for l in range(j - 1, j + 2):
                if 0 <= k < 8 and 0 <= l < 8:
                    middle = [k, l] == [i, j]
                    safe = board[k][l] == 3
                    isolated_amazon = amazon == [k, l] and not near_king(k, l)
                    spot_num += not middle and (safe or isolated_amazon)
                    
        return spot_num
    
    for i in range(8):
        for j in range(8):
            if near_king(i, j) or amazon == [i, j]:
                board[i][j] = -1
                
            elif under_attack(i, j):
                board[i][j] = 1
                
    for i in range(8):
        for j in range(8):
            if board[i][j] == -1:
                continue
                
            if safe_spot_num(i, j):
                if board[i][j] == 3:
                    result[3] += 1
                
                if board[i][j] == 1:
                    result[1] += 1
            else:
                if board[i][j] == 3:
                    result[2] += 1
                
                if board[i][j] == 1:
                    result[0] += 1
                    
    return result
