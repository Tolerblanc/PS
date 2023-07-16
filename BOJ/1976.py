import sys

input = sys.stdin.readline

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

n = int(input())
parent = [x for x in range(n + 1)]
m = int(input())
graph = [[]]
for _ in range(n):
    graph.append(list(map(int, input().split())))
schedule = list(map(int ,input().split()))

for i in range(1, n + 1):
    for j in range(n):
        if graph[i][j] > 0:
            if find(parent, i) != find(parent, j + 1):
                union(parent, i, j + 1)

answer = len(set([find(parent, x) for x in schedule]))
if answer == 1:
    print('YES')
else:
    print('NO')