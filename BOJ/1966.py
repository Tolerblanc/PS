import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    priority = deque([(x, i) for i, x in enumerate(list(map(int, input().split())))])
    cnt = 0
    while priority:
        localMax = max(priority)
        while priority[0][0] != localMax[0]:
            priority.append(priority.popleft())
        if priority.popleft()[1] == m:
            break
        cnt += 1
    print(cnt + 1)