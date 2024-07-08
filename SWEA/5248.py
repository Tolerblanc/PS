def union(parents, a, b):
    a = find(parents, a)
    b = find(parents, b)
    if a < b:
        parents[b] = a
    else:
        parents[a] = b


def find(parents, x):
    if parents[x] != x:
        parents[x] = find(parents, parents[x])
    return parents[x]


for tc in range(int(input())):
    n, m = map(int, input().split())
    query = list(map(int, input().split()))
    parents = [i for i in range(n + 1)]
    for i in range(m):
        union(parents, query[2 * i], query[2 * i + 1])
    for i in range(1, n + 1):
        find(parents, i)
    print(f'#{tc + 1} {len(set(parents)) - 1}')
