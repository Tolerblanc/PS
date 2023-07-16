import sys, heapq

input = sys.stdin.readline

h = []
n = int(input())
for _ in range(n):
    heapq.heappush(h, int(input()))

result = 0
while len(h) >= 2:
    temp = heapq.heappop(h) + heapq.heappop(h)
    result += temp
    heapq.heappush(h, temp)
print(result)