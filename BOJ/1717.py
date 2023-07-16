import sys

#sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

def find_p(parent, x):
    if parent[x] != x:
        parent[x] = find_p(parent, parent[x])
    return parent[x]

def union_p(parent, a, b):
    a = find_p(parent, a)
    b = find_p(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().rstrip().split())
graph = [x for x in range(n + 1)]

for _ in range(m):
    oper, a, b = map(int, input().rstrip().split())
    if oper == 0:
        union_p(graph, a, b)
    else:
        if find_p(graph, a) == find_p(graph, b):
            print('YES')
        else:
            print('NO')