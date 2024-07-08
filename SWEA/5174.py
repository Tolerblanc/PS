for tc in range(int(input())):
    e, n = map(int, input().split())
    left = [0] * (e + 2)
    right = [0] * (e + 2)
    edges = list(map(int, input().split()))
    for i in range(e):
        parent, child = edges[i * 2], edges[i * 2 + 1]
        if left[parent] == 0:
            left[parent] = child
        else:
            right[parent] = child

    def dfs(curr, depth):
        l = dfs(left[curr], depth + 1) if left[curr] else 0
        r = dfs(right[curr], depth + 1) if right[curr] else 0
        return l + r + 1

    print(f'#{tc + 1} {dfs(n, 1)}')
