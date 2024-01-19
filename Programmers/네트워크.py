def find(parents, a):
    if parents[a] != a:
        parents[a] = find(parents, parents[a])
    return parents[a]


def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if parents[a] < parents[b]:
        parents[b] = parents[a]
    else:
        parents[a] = parents[b]


def solution(n, computers):
    parents = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and parents[i] != parents[j]:
                union(parents, i, j)
    for i in range(n):
        find(parents, i)
    return len(set(parents))
