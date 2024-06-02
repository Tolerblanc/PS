import sys
import heapq
input = sys.stdin.readline

heap = []
N = int(input())
for _ in range(N):
    for num in map(int, input().split()):
        heapq.heappush(heap, num)
        if len(heap) > N:
            heapq.heappop(heap)
    print(heap)
print(heap[0])
