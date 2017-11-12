#coding: utf-8

def zero_matrix(matrix, M, N):

	row_to_zero = []
	col_to_zero = []
	for i in range(m):
		for j in range(n):
			if matrix[i][j] == 0:
				col_to_zero.append(j)
				row_to_zero.append(i)

	for row in row_to_zero:
		for i in range(n):
			matrix[row][i] = 0
	for col in col_to_zero:
		for j in range(m):
			matrix[j][col] = 0

