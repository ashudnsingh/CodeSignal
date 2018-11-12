def merge(row, left_or_down):
    i, new_row = 0, []
    transposed = [e for e in row if e]

    if not left_or_down: 
        transposed = transposed[::-1]

    while i < len(transposed):
        if i == len(transposed) - 1:
            new_row += [transposed[i]]
            break
        if transposed[i] == transposed[i + 1]:
            new_row += [2 * transposed[i]]
            i += 2
        else:
            new_row += [transposed[i]]
            i += 1

    if not left_or_down: 
        new_row = [0]*(4 - len(new_row)) + new_row[::-1]

    return  new_row + [0]*(4 - len(new_row))

def game2048(grid, path):    
    for direc in path:

        if direc in 'LR':
            grid = [merge(row, direc == 'L') for row in grid]

        if direc in 'UD':
            grid = [merge(row[::-1], direc == 'D') for row in zip(*grid)]
            grid = [row for row in zip(*grid)][::-1]

    return grid
