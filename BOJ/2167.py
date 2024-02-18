import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

acc = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        acc[i][j] = arr[i][j]
        if i > 0:
            acc[i][j] += acc[i-1][j]
        if j > 0:
            acc[i][j] += acc[i][j-1]
        if i > 0 and j > 0:
            acc[i][j] -= acc[i-1][j-1]

for _ in range(int(input())):
    i, j, x, y = map(int, input().split())
    answer = acc[x-1][y-1]
    if i > 1:
        answer -= acc[i-2][y-1]
    if j > 1:
        answer -= acc[x-1][j-2]
    if i > 1 and j > 1:
        answer += acc[i-2][j-2]
    print(answer)
