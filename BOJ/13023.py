import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    lst[a].append(b)
    lst[b].append(a)

def dfs(idx, depth, visited):
    if (depth == 4):
        return 1
    visited[idx] = True
    for n in lst[idx]:
        if visited[n] == True:
            continue
        if (dfs(n, depth + 1, visited) == 1):
            return 1
    visited[idx] = False
    return 0

def solve():
    for i in range(n):
        visited = [False] * n
        if (dfs(i, 0, visited) == 1):
            print(1)
            return
    else:
        print(0)
        return

solve()