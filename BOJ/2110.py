import sys
input = sys.stdin.readline

n, c = map(int, input().split())
routers = []
for _ in range(n):
    routers.append(int(input()))
routers.sort()


def check(dist):
    cnt = 1
    prev = routers[0]
    for router in routers[1:]:
        if router - prev >= dist:
            cnt += 1
            prev = router
    return True if cnt >= c else False


l, r = 0, 1_000_000_001
answer = 0
while l <= r:
    mid = (l + r) // 2
    if check(mid):
        answer = max(answer, mid)
        l = mid + 1
    else:
        r = mid - 1
print(answer)
