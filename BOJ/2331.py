import sys
input = sys.stdin.readline

a, p = map(int, input().split())
visited = [a]


def dfs(n, p):
    curr = sum([int(k) ** p for k in str(n)])
    if curr in visited:
        return visited.index(curr)
    visited.append(curr)
    return dfs(curr, p)


print(dfs(a, p))
