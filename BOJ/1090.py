import sys
input = sys.stdin.readline

N = int(input())
answer = [100_000_001] * N
coordinates, X, Y = [], [], []

for _ in range(N):
    x, y = map(int, input().split())
    coordinates.append((x, y))
    X.append(x)
    Y.append(y)

for x in X:
    for y in Y:
        acc = 0  # 거리 누적합
        dists = [abs(a - x) + abs(b - y) for a, b in coordinates]
        dists.sort()
        for i in range(N):
            acc += dists[i]
            answer[i] = min(answer[i], acc)

print(*answer)
