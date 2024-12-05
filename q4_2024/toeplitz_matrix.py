# Toeplitz matrix

mat = [[1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 2]]

nmat = [[1, 2, 3, 4, 8],
        [5, 1, 2, 3, 4],
        [4, 5, 1, 2, 3],
        [7, 4, 5, 1, 5]]



def find_toeplitz_matrix(m):

    rows = len(m)
    cols = len(m[0])
    for i in range(1, rows):
        for j in range(1, cols):
            if (m[i][j] != m[i-1][j-1]):
                return False     
    return True

print(find_toeplitz_matrix(mat))
print(find_toeplitz_matrix(nmat))