import sys
input = sys.stdin.readline

n, b = map(int, input().split())
result = []

while n:
    q, r = divmod(n, b)
    result.append(str(r) if r < 10 else chr(ord('A') + r - 10))
    n = q
print(''.join(result[::-1]))
