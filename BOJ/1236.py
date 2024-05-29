import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]

for g in graph:
    if 'X' in g:
        n -= 1

for g in list(zip(*graph)):
    if 'X' in g:
        m -= 1

print(max(n, m))
