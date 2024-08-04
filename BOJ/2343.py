import sys
from math import ceil
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def check(size):
    cnt = 0
    rec = 0
    for n in nums:
        if rec + n > size:
            cnt += ceil(rec / size)
            rec = n
        else:
            rec += n
    return cnt < m and rec <= size


left = 1
right = answer = 10 ** 9 + 1
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1
print(answer)
