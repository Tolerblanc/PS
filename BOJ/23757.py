import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())

presents = list(map(lambda x: -int(x), input().split()))
children = list(map(int, input().split()))

heapq.heapify(presents)


def solve():
    for cnt in children:
        if not presents:
            return 0
        now = -heapq.heappop(presents)
        if cnt > now:
            return 0
        if cnt < now:
            heapq.heappush(presents, -(now - cnt))
    return 1


print(solve())
