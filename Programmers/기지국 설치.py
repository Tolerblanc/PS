import math


def solution(n, stations, w):
    COVERAGE = 2 * w + 1
    answer = 0 if stations[0] - \
        w <= 1 else math.ceil((stations[0] - w - 1) / COVERAGE)
    prev = stations[0] + w
    for station in stations[1:]:
        answer += 0 if station - w - \
            prev <= 1 else math.ceil((station - w - prev - 1) / COVERAGE)
        prev = station + w
    return answer if prev >= n else answer + math.ceil((n - prev) / COVERAGE)
