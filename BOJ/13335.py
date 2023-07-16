import sys
from collections import deque
input = sys.stdin.readline

n, w, l = map(int, input().split())
trucks = list(map(int, input().split()))
idx = 0
q = deque([0 for _ in range(w)])
time = 0
suffix = 0

while idx < n:
    suffix -= q.popleft()
    next = 0
    if suffix + trucks[idx] <= l:
        next = trucks[idx]
        idx += 1
    suffix += next
    q.append(next)
    time += 1

print(time + w)