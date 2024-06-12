import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = [i + 1 for i in range(n)]
for _ in range(m):
    i, j = map(int, input().split())
    lst[i-1], lst[j-1] = lst[j-1], lst[i-1]
print(*lst)
