import sys
input = sys.stdin.readline

n = int(input())
local = list(map(int, input().split()))
gov = int(input())

answer = 0
left, right = 1, max(local)
while left <= right:
    mid = (left + right) // 2
    if sum([min(mid, num) for num in local]) <= gov:
        answer = max(answer, mid)
        left = mid + 1
    else:
        right = mid - 1
print(answer)
