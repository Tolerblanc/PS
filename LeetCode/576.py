class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0:
            return 0

        dr = [1, 0, -1, 0]
        dc = [0, 1, 0, -1]
        MOD = 10 ** 9 + 7

        graph = [[[0] * (maxMove) for _ in range(n)] for _ in range(m)]
        graph[startRow][startColumn][0] = 1
        for move in range(1, maxMove):
            for row in range(m):
                for col in range(n):
                    if graph[row][col][move - 1] != 0:
                        for i in range(4):
                            nr, nc = row + dr[i], col + dc[i]
                            if nr < 0 or nc < 0 or nr >= m or nc >= n:
                                continue
                            graph[nr][nc][move] += graph[row][col][move - 1]
        for row in range(m):
            for col in range(n):
                graph[row][col] = sum(graph[row][col])
        vertical = list(zip(*graph))
        answer = 0
        answer += sum(graph[0])
        answer += sum(graph[-1])
        answer += sum(vertical[0])
        answer += sum(vertical[-1])
        return answer % MOD
