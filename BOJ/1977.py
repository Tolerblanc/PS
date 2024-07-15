import sys
input = sys.stdin.readline

m = int(input())
n = int(input())

minimum, total = 99999, 0
for i in range(m, n + 1):
    if i ** 0.5 == int(i ** 0.5):
        total += i
        minimum = min(i, minimum)

if total == 0:
    print(-1)
else:
    print(total)
    print(minimum)
