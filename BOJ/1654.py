import sys
input = sys.stdin.readline

k, n = map(int, input().split())
lan = [int(input()) for _ in range(k)]


def check(value):
    cnt = 0
    for l in lan:
        cnt += l // value
    return cnt >= n


answer = 0
left, right = 0, 2147483647
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)
