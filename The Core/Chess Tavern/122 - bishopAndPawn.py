def bishopAndPawn(bishop, pawn):
    return abs(ord(bishop[0])-ord(pawn[0]))==abs(int(pawn[1])-int(bishop[1]))
