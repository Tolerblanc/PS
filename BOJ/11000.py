import sys
input = sys.stdin.readline

count = 0
n = int(input())
classes = []
for _ in range(n):
    s, e = map(int, input().split())
    classes.append((s, 1))
    classes.append((e, -1))
classes.sort()

acc = 0
for _, v in classes:
    acc += v
    count = max(count, acc)
print(count)
