import sys

input = sys.stdin.readline

g = int(input())
p = int(input())

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

parent = [x for x in range(g + 1)]

planes = []
for i in range(p):
    planes.append(int(input()))

cnt = 0
for i in planes:
    k = find(parent, i)
    if k == 0:
        break
    union(parent, k, k-1)
    cnt += 1
print(cnt)