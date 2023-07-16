import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
blues = list(map(int, input().split()))
reds = list(map(int, input().split()))

blues.sort()

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

parent = [x for x in range(n + 1)]

for r in reds:
    start = 0
    end = m - 1
    while start < end:
        mid = (start + end) // 2
        #print(start, end, mid, r, find(parent, blues[mid]))
        if r >= find(parent, blues[mid]):
            start = mid + 1
        else:
            end = mid
    print(blues[end])
    if end == 0:
        union(parent, 0, blues[0])
    else:
        union(parent, blues[end], blues[end - 1])