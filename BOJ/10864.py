import sys
input = sys.stdin.readline

n, m = map(int, input().split())
status = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    status[a] += 1
    status[b] += 1
print(*status[1:], sep='\n')
