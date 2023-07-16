import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
line = [0] * 100001
q = deque()
line[n] = 0
q.append(n)

while q:
    now = q.popleft()
    if now == m:
        print(line[now])
        break
    
    next = (now + 1, now - 1, now * 2)
    for ne in next:
        if ne >= 0 and ne <= 100000 and not line[ne]:
            q.append(ne)
            line[ne] = line[now] + 1