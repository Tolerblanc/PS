import sys
input = sys.stdin.readline

c, r = map(int, input().split())
k = int(input())
if c * r < k:
    print(0)
    exit()
if k == 1:
    print(1, 1)
    exit()

graph = [[0] * c for _ in range(r)]
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

x, y = r - 1, 0
graph[x][y] = 1
direction = 0
curr = 1
while True:
    nx, ny = x + dr[direction], y + dc[direction]
    if nx < 0 or ny < 0 or nx >= r or ny >= c or graph[nx][ny]:
        direction = (direction + 1) % 4
        continue
    curr += 1
    if curr == k:
        print(ny + 1, r - nx)
        break
    graph[nx][ny] = curr
    x, y = nx, ny
