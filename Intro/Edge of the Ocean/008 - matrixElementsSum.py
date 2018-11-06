def matrixElementsSum(matrix):
    rowLen = matrix.__len__();
    colLen = matrix[0].__len__();
    sumNum = 0;
    col    = 0
    while col < colLen :
        row  = 0
        while row < rowLen:
            if  matrix[row][col] != 0 :
                sumNum += matrix[row][col]
            else :
                break
            row += 1
        col += 1
    return sumNum
