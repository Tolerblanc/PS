import sys
input = sys.stdin.readline

n = int(input())
pick = []
visited = [False] * (n + 1)


def backtracking(depth):
    if depth == n:
        print(*pick)
    for i in range(1, n + 1):
        if visited[i]:
            continue
        visited[i] = True
        pick.append(i)
        backtracking(depth + 1)
        pick.pop()
        visited[i] = False


backtracking(0)
