import sys, heapq

#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input().rstrip())
h = []
for _ in range(n):
    inp = int(input().rstrip())
    if inp != 0:
        heapq.heappush(h, (abs(inp), inp))
    else:
        if h:
            a, b = heapq.heappop(h)
            print(b)
        else:
            print(0)