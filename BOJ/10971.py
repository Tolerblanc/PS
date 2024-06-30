import sys
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
answer = int(1e9)
visited = [False] * n


def backtracking(curr, cost, depth):
    global answer
    if depth == n:
        if graph[curr][0]:
            answer = min(answer, cost + graph[curr][0])
        return
    if cost > answer:
        return
    for i in range(n):
        if not visited[i] and graph[curr][i]:
            visited[i] = True
            backtracking(i, cost + graph[curr][i], depth + 1)
            visited[i] = False


visited[0] = True
backtracking(0, 0, 1)
print(answer)
