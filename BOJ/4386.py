import sys, heapq, math

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
parent = [i for i in range(n + 1)]
dots = [0]
for i in range(n):
    x, y = map(float, input().split())
    dots.append((x,y))

q = []
for i in range(1, n):
    x1, y1 = dots[i]
    for j in range(i, n + 1):
        x2, y2 = dots[j]
        dist = round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 2)
        heapq.heappush(q, (dist, i, j))

cnt = 0
result = 0
while cnt < n - 1:
    cost, a, b = heapq.heappop(q)
    if find(parent, a) != find(parent, b):
        result += cost
        union(parent, a, b)
        cnt += 1
print(result)