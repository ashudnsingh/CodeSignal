def pawnRace(white, black, move):
    move = 'black' if move == 'b' else 'white'
    wy, wx = int(white[1]) - 1, ord(white[0]) - ord('a')
    by, bx = int(black[1]) - 1, ord(black[0]) - ord('a')

    if wx == bx and by > wy:
        return 'draw'

    curr = 'black' if move == 'white' else 'white'
    while wy < 7 and by > 0:
        curr = 'black' if curr == 'white' else 'white'
        diff = by - wy
        if diff == 1:
            break

        if curr == 'black':
            by -= (2 if by == 6 and diff != 3 else 1)
        else:
            wy += (2 if wy == 1 and diff != 3 else 1)

    return curr
