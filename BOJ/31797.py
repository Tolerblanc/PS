import sys
input = sys.stdin.readline

n, m = map(int, input().split())
att = []
for i in range(m):
    x, y = map(int, input().split())
    att.append((x, i + 1))
    att.append((y, i + 1))

att.sort()
print(att[n % (2 * m) - 1][1])
