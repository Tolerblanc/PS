import sys
input = sys.stdin.readline

n = int(input())
prev = -1000000001
total = 0
lines = []
for _ in range(n):
    x, y = map(int, input().split())
    lines.append((x, y))
lines.sort()

for x, y in lines:
    if y <= prev:
        continue
    if x >= prev:
        total += y - x
    else:
        total += y - prev
    prev = y
print(total)
