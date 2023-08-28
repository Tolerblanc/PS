import sys
input = sys.stdin.readline

n, l = map(int, input().split())
lst = list(map(int, input().split()))

answer = 0
suffix = 0
for i in range(n):
    suffix += lst[i]
    if i - l >= 0:
        suffix -= lst[i - l]
    if 129 <= suffix <= 138:
        answer += 1

print(answer)
