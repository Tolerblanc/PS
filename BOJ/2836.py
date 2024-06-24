import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rev = []
for _ in range(n):
    s, e = map(int, input().split())
    if s > e:
        rev.append((e, s))

rev.sort()
answer = left = right = 0
for l, r in rev:
    if l <= right:
        right = max(r, right)
    else:
        answer += right - left
        left = l
        right = r
answer += right - left
print(answer * 2 + m)
