import heapq


def solution(n, works):
    total = sum(works)
    for i in range(len(works)):
        works[i] *= -1
    heapq.heapify(works)
    while n > 0 and total > 0:
        localMax = heapq.heappop(works)
        heapq.heappush(works, localMax + 1)
        n -= 1
        total -= 1
    return sum([n * n for n in works])
