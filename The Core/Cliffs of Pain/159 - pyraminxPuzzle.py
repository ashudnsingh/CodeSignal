def pyraminxPuzzle(face_colours, moves):
    move_position = { "U": [[0, 0], [3, 8], [2, 4]],
                      "u": [[0, 0], [0, 1], [0, 2], [0, 3], [3, 8], [3, 3], [3, 7], [3, 6], [2, 4], [2, 6], [2, 5], [2, 1]],
                      "L": [[2, 0], [1, 8], [0, 4]],
                      "l": [[2, 0], [2, 1], [2, 2], [2, 3], [1, 8], [1, 3], [1, 7], [1, 6], [0, 4], [0, 6], [0, 5], [0, 1]],
                      "R": [[3, 0], [0, 8], [1, 4]],
                      "r": [[3, 0], [3, 1], [3, 2], [3, 3], [0, 3], [0, 8], [0, 7], [0, 6], [1, 4], [1, 6], [1, 5], [1, 1]],
                      "B": [[1, 0], [2, 8], [3, 4]],
                      "b": [[1, 0], [1, 1], [1, 2], [1, 3], [2, 8], [2, 3], [2, 7], [2, 6], [3, 4], [3, 6], [3, 5], [3, 1]] }

    puzzle = [[c for _ in range(9)] for c in face_colours]
    for move in reversed(moves):
        left = "'" not in move
        move_colors = { move: [puzzle[r][c] for r, c in move_position[move]] for move in move_position }
        current_color = shift_color(move_colors[move[0]], left)        
        for idx, pos in enumerate(move_position[move[0]]):
            puzzle[pos[0]][pos[1]] = current_color[idx]

    return puzzle

def shift_color(current_color, left):
    i = len(current_color) // 3
    if left:
        return current_color[i:] + current_color[0:i]
    return current_color[-i:] + current_color[:-i]
