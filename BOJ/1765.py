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
enemy = [[] for _ in range (n + 1)]
friend = []

m = int(input())
for _ in range(m):
    rel, p, q = input().split()
    p = int(p)
    q = int(q)
    if rel[0] == 'F':
        friend.append((p, q))
    elif rel[0] == 'E':
        enemy[p].append(q)
        enemy[q].append(p)

for i in range(1, n + 1):
    if len(enemy[i]) == 0:
        continue
    for e in enemy[i]:
        for f in enemy[e]:
            union(parent, i, f)

for f in friend:
    union(parent, f[0], f[1])

for i in range(1, n + 1):
    find(parent, i)

print(len(set(parent)) - 1)