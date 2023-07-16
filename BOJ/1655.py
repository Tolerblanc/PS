import sys, heapq

input = sys.stdin.readline

l = []
r = []
mid = 0

n = int(input())
for i in range(1, n + 1):
    num = int(input())
    if i % 2 == 1:
        if i == 1:
            mid = num
        else:
            if -l[0] < num < r[0]:
                mid = num
            elif -l[0] >= num:
                mid = -heapq.heapreplace(l, -num)
            else:
                mid = heapq.heapreplace(r, num)
    else:
        if num >= mid:
            heapq.heappush(l, -mid)
            heapq.heappush(r, num)
        else:
            heapq.heappush(l, -num)
            heapq.heappush(r, mid)
        mid = -l[0]
    print(mid)