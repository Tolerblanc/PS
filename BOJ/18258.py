import sys
from collections import deque
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    comm, *arg = input().split()
    if comm == 'push':
        q.append(int(arg[0]))
    elif comm == 'pop':
        print(q.popleft() if q else -1)
    elif comm == 'size':
        print(len(q))
    elif comm == 'empty':
        print(1 if not q else 0)
    elif comm == 'front':
        print(q[0] if q else -1)
    elif comm == 'back':
        print(q[-1] if q else -1)
