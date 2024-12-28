def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for a in range(m):
            matrix[i].append(value)
    print(matrix)
    return matrix
print(get_matrix(3, 6, 10))