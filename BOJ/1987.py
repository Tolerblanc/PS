import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline

r, c = map(int, input().rstrip().split()) 
graph = []
for _ in range(r):
    graph.append(input().rstrip())
    
visited = [[False] * c for _ in range(r)]
used = [False] * 26

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
result = 0

def dfs(row, col, cnt):
    global result
    result = max(cnt, result)
    if row < 0 or col < 0 or row >= r or col >= c:
        return
    visited[row][col] = True
    used[ord(graph[row][col]) - ord('A')] = True
    for i in range(4):
        nr = row + dx[i]
        nc = col + dy[i]
        if nr < 0 or nc < 0 or nr >= r or nc >= c or visited[nr][nc]:
            continue
        if not used[ord(graph[nr][nc]) - ord('A')]:
            dfs(nr, nc, cnt + 1)
    visited[row][col] = False
    used[ord(graph[row][col]) - ord('A')] = False
    
dfs(0, 0, 1)
print(result)