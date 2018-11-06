def polygonPerimeter(matrix):
    return (4 * sum(map(sum, matrix)) - 2 * (
        sum(a and b for row in matrix for a, b in zip(row, row[1:])) +
        sum(a and b for row in zip(*matrix) for a, b in zip(row, row[1:]))))
