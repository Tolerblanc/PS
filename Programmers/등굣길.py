def solution(m, n, puddles):
    MOD = 1_000_000_007
    graph = [[1] * m for _ in range(n)]
    for puddle in puddles:
        graph[puddle[1] - 1][puddle[0] - 1] = 0
        if puddle[0] == 1:
            for i in range(puddle[1] - 1, n):
                graph[i][0] = 0
        if puddle[1] == 1:
            for i in range(puddle[0] - 1, m):
                graph[0][i] = 0

    for r in range(1, n):
        for c in range(1, m):
            if graph[r][c] == 0:
                continue
            graph[r][c] = graph[r-1][c] + graph[r][c-1]

    return graph[n - 1][m - 1] % MOD
