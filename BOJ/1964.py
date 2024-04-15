import sys
input = sys.stdin.readline

n = int(input())
print((1 + n + 3 * n * (n + 1) // 2) % 45678)
