import sys
input = sys.stdin.readline

n, b = map(int, input().split())
matrix = []
for _ in range(n):
	matrix.append(list(map(int, input().split())))

def mat_mul(a, b, size):
	result = [[0] * size for _ in range(size)]

	if (b == 0):
		for i in range(size):
			for j in range(size):
				result[i][j] = a[i][j] % 1000
		return result

	for i in range(size):
		for j in range(size):
			for k in range(size):
				result[i][j] += a[i][k] * b[k][j]
				result[i][j] %= 1000
	
	return result

def mat_power(mat, size, power):
	if (power == 1):
		return mat
	if (power % 2 == 0):
		return mat_power(mat_mul(mat, mat, size), size, power // 2)
	else:
		return mat_mul(mat_power(mat_mul(mat, mat, size), size, power // 2), mat, size)

matrix = mat_power(matrix, n, b)
if (b == 1):
	matrix = mat_mul(matrix, 0, n)
for m in matrix:
	print(*m)