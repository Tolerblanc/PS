import sys

sys.stdin = open('input.txt')
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


n, m = map(int, input().rstrip().split())
parent = [x for x in range(n + 1)]
cycle = False
for i in range(m):
    a, b = map(int, input().rstrip().split())
    if find(parent, a) == find(parent, b):
        print(i + 1)
        break
    else:
        union(parent, a, b)
else:
    print(0)