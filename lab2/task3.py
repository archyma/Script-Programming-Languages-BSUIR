def matr(matrix):
    rowsPos = all(any(i > 0 for i in row) for row in matrix)

    if rowsPos:
        matrix = [[-i for i in row] for row in matrix]

    return matrix
print(matr([[1,-2,3],[4,-5,-6],[7,8,-9]]))

print(matr([[-1,0,-3],[-4,-5,-6],[-7,-8,-9]]))