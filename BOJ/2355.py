import sys
input = sys.stdin.readline

a, b = map(int, input().split())
a, b = min(a, b), max(a, b)

print((b * (b + 1) // 2) - (a * (a + 1) // 2) + a)
