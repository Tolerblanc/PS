import sys
input = sys.stdin.readline

d, n, m = map(int, input().split())
left, right = 0, d
islands = sorted([int(input()) for _ in range(n)])


def check(dist):
    cnt, last = 0, 0
    for island in islands:
        if island - last < dist:
            cnt += 1
        else:
            last = island
    return cnt <= m and d - last >= dist


while left <= right:
    mid = (left + right) // 2
    if check(mid):
        result = mid
        left = mid + 1
    else:
        right = mid - 1

print(result)
