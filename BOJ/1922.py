import sys
input = sys.stdin.readline

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent ,a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n = int(input())
edges = []
parent = [i for i in range(0, n + 1)]

m = int(input())
for _ in range(m):
    src, dst, cost = map(int, input().split())
    edges.append((cost, src, dst))

edges.sort()
answer = 0
for edge in edges:
    cost, src, dst = edge
    if find(parent, src) != find(parent, dst):
        answer += cost
        union(parent, src, dst)
print(answer)
