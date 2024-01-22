def check(interval, dist, n):
    cnt = 0  # 없앤 바위 수
    curr = 0  # 간격 누적
    for i in range(len(interval)):
        curr += interval[i]
        if curr >= dist:  # 간격이 최소 거리를 넘었으면 초기화
            curr = 0
        else:  # 아니면, 계속 누적하고 없애야 하는 바위 수 +1
            cnt += 1
            if cnt > n:  # 한계치 이상 없앴으면 False
                return False
    return True


def solution(distance, rocks, n):
    interval = []
    rocks.sort()
    interval.append(rocks[0])
    for i in range(1, len(rocks)):
        interval.append(rocks[i] - rocks[i - 1])
    interval.append(distance - rocks[-1])

    l = 1
    r = distance
    while l <= r:
        mid = (l + r) // 2
        if check(interval, mid, n):
            answer = mid
            l = mid + 1
        else:
            r = mid - 1
    return answer
