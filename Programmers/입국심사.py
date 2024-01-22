def check(n, times, limit):
    complete = 0
    for time in times:
        complete += limit // time
    return True if complete >= n else False


def solution(n, times):
    left = 1
    right = max(times) * n
    while left <= right:
        mid = (left + right) // 2
        if check(n, times, mid):
            answer = mid
            right = mid - 1
        else:
            left = mid + 1
    return answer
