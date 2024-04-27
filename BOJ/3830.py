import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)


def find(x, parent, value, parentvalue):
    if parent[x] != x:
        p, pv = parent[x], parentvalue[x]
        parent[x] = find(p, parent, value, parentvalue)
        value[x] += value[p] - pv
        parentvalue[x] = value[parent[x]]
    return parent[x]


def union(a, b, w, parent, value, parentvalue):
    value[a] -= w
    parent[a] = b
    parentvalue[a] = value[b]


while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    parent = [i for i in range(n + 1)]
    value = [0] * (n + 1)
    parentvalue = [0] * (n + 1)

    for _ in range(m):
        query, *param = input().split()
        if query == '?':
            a, b = map(int, param)
            print(value[b] - value[a] if find(a, parent, value, parentvalue)
                  == find(b, parent, value, parentvalue) else "UNKNOWN")
            continue
        a, b, w = map(int, param)
        if find(a, parent, value, parentvalue) != find(b, parent, value, parentvalue):
            union(parent[a], parent[b], w - value[b] +
                  value[a], parent, value, parentvalue)
