import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))


def check(mid):
    low = high = nums[0]
    part = 0
    for num in nums[1:]:
        low = min(low, num)
        high = max(high, num)
        if high - low > mid:
            part += 1
            low = high = num
    return part + 1 <= m


left, right = 0, 50000001
answer = right
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = min(answer, mid)
        right = mid - 1
    else:
        left = mid + 1

print(answer)
