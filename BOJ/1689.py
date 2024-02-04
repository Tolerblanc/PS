import sys
input = sys.stdin.readline

n = int(input())
points = []
for _ in range(n):
    s, e = map(int, input().split())
    points.append((s, 1))
    points.append((e, -1))
points.sort()

pSum = 0
answer = 0
for x, v in points:
    pSum += v
    answer = max(answer, pSum)
print(answer)
