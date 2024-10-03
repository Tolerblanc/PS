import sys
input = sys.stdin.readline

k = int(input())
N = 1 << k
graph = [[0] * N for _ in range(N)]
hx, hy = map(int, input().split())
hx, hy = N - hy, hx - 1
graph[hx][hy] = -1
seq = 0


def check(lx, ly, length):
    for i in range(lx, lx + length):
        for j in range(ly, ly + length):
            if graph[i][j] != 0:
                return False
    return True


def recur(lx, ly, length):
    global seq
    seq += 1
    half = length // 2
    if check(lx, ly, half):
        graph[lx + half - 1][ly + half - 1] = seq
    if check(lx + half, ly, half):
        graph[lx + half][ly + half - 1] = seq
    if check(lx, ly + half, half):
        graph[lx + half - 1][ly + half] = seq
    if check(lx + half, ly + half, half):
        graph[lx + half][ly + half] = seq
    if length == 2:
        return

    recur(lx, ly, half)
    recur(lx + half, ly, half)
    recur(lx, ly + half, half)
    recur(lx + half, ly + half, half)


recur(0, 0, N)
for row in graph:
    print(*row)
