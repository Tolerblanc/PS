import sys
input = sys.stdin.readline

n, k = map(int, input().split())
scores = list(map(int, input().split()))

left, right = 0, 20 * 10 ** 5 + 1
answer = -1


def check(val):
    cnt = 0
    acc = 0
    for score in scores:
        acc += score
        if acc >= val:
            acc = 0
            cnt += 1
    return cnt >= k


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)
