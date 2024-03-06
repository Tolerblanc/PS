import sys
import heapq
input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))
heapq.heapify(nums)

for _ in range(m):
    card1 = heapq.heappop(nums)
    card2 = heapq.heappop(nums)
    heapq.heappush(nums, card1 + card2)
    heapq.heappush(nums, card1 + card2)

print(sum(nums))
