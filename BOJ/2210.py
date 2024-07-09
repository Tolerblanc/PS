import sys
input = sys.stdin.readline

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
graph = [input().split() for _ in range(5)]
answer = set()
pick = []


def dfs(depth, r, c):
    if depth == 6:
        answer.add(int(''.join(pick)))
        return
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if nr < 0 or nc < 0 or nr >= 5 or nc >= 5:
            continue
        pick.append(graph[nr][nc])
        dfs(depth + 1, nr, nc)
        pick.pop()


for i in range(5):
    for j in range(5):
        dfs(0, i, j)
print(len(answer))
