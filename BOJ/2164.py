import sys
from collections import deque

n = int(sys.stdin.readline())
q = deque([x for x in range(1, n + 1)])
while q:
    a = q.popleft()
    if not q:
        break
    b = q.popleft()
    q.append(b)
print(a)