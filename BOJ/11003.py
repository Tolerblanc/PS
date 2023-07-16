import sys, heapq

input = sys.stdin.readline

n, l = map(int, input().split())
lst = map(int, input().split())
left = right = 0

pq = []
for i, v in enumerate(lst):
    heapq.heappush(pq, (v, i))
    left = i - l + 1 if i >= l else 0
    right = i
    while pq[0][1] < left:
        heapq.heappop(pq)
    if i < n - 1:
        print(pq[0][0], end = ' ')
    else:
        print(pq[0][0], end = '')