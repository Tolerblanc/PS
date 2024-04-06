import sys
import heapq
input = sys.stdin.readline

n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]

heapq.heapify(gems)
bags.sort()

result = 0
price = []

for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(price, -heapq.heappop(gems)[1])
    result += -heapq.heappop(price) if price else 0
print(result)
