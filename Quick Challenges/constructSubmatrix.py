def constructSubmatrix(matrix, delRows, delCols):
    for x in delRows:
        matrix = [i for i in matrix if i is not matrix[x]]
    offset = 0
    for y in delCols:
        matrix = [i[:y-offset] + i[y+1-offset:] for i in matrix]
        offset += 1
    return matrix
