import sys
input = sys.stdin.readline

n = int(input())
mines = [list(input().rstrip()) for _ in range(n)]
opened = [list(input().rstrip()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]
dr = [1, 0, -1, 0, 1, 1, -1, -1]
dc = [0, 1, 0, -1, 1, -1, -1, 1]


def check(r, c):
    if mines[r][c] == '*':
        answer[r][c] = '*'
        return
    elif opened[r][c] == '.':
        return
    mine = 0
    for i in range(8):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nc < 0 or nr >= n or nc >= n:
            continue
        mine += 1 if mines[nr][nc] == '*' else 0
    answer[r][c] = str(mine)


mine_boomed = False
for i in range(n):
    for j in range(n):
        if opened[i][j] == 'x':
            check(i, j)
            if mines[i][j] == '*':
                mine_boomed = True

if mine_boomed:
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    print(''.join(answer[i]))
