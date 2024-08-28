import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().split())
print(abs((d + a) - (b + c)))
