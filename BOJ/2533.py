import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(1000001)

INF = 1000000001
n = int(input().rstrip())
dp = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().rstrip().split())
    dp[u].append(v)
    dp[v].append(u)

child = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

def dfs(curr):
    visited[curr] = True
    for next in dp[curr]:
        if not visited[next]:
            child[curr].append(next)
            dfs(next)

dfs(1)

dp = [[-1] * 2 for _ in range(n + 1)]

def sns(curr, is_ped): #curr node, bool_parent is early adaptor(0, 1)
    if dp[curr][is_ped] != -1:
        return dp[curr][is_ped]
    np = INF
    p = 1
    for next in child[curr]:
        p += sns(next, 1)
    if is_ped:
        np = 0
        for next in child[curr]:
            np += sns(next, 0)
    dp[curr][is_ped] = min(np, p)
    return dp[curr][is_ped]

print(sns(1, 1))