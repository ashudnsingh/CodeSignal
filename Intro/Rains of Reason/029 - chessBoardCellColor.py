def chessBoardCellColor(cell1, cell2):
    return True if ( ord( list(cell1)[0] ) + int(list(cell1)[1]) ) % 2 == ( ord(list(cell2)[0]) + int(list(cell2)[1]) ) % 2 else False
