import sys

sys.setrecursionlimit(100001)
input = sys.stdin.readline

v, e = map(int, input().split())


def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]


def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


parent = [i for i in range(v + 1)]
edges = []

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

result = 0
edges.sort()
for edge in edges:
    cost, a, b = edge
    if find(parent, a) != find(parent, b):
        result += cost
        union(parent, a, b)
print(result)
