for tc in range(int(input())):
    n, m = map(int, input().split())
    graph = [list(map(int, input().split())) for _ in range(n)]
    answer = 0
    for r in range(n - m + 1):
        for c in range(n - m + 1):
            tmp = 0
            for i in range(m):
                for j in range(m):
                    tmp += graph[i + r][j + c]
            answer = max(answer, tmp)
    print(f'#{tc + 1} {answer}')
