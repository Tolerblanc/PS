dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for i in range(n):
        for j in range(m):
            tmp = graph[i][j]
            for k in range(4):
                if i + dr[k] < 0 or j + dc[k] < 0 or i + dr[k] >= n or j + dc[k] >= m:
                    continue
                tmp += graph[i + dr[k]][j + dc[k]]
            answer = max(answer, tmp)
    print(f'#{tc + 1} {answer}')
