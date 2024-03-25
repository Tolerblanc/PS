import sys
input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    _, s, e = map(int, input().split())
    classes.append((s, 1))
    classes.append((e, -1))
classes.sort()
prefix = 0
answer = 0
for x, v in classes:
    prefix += v
    answer = max(answer, prefix)
print(answer)
