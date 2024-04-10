from collections import deque
import sys
input = sys.stdin.readline

q = deque()
for _ in range(int(input())):
    inp = input().split()
    comm, num = inp if len(inp) > 1 else (inp[0], None)
    if comm == 'push':
        q.append(int(num))
    elif comm == 'front':
        print(q[0] if len(q) else -1)
    elif comm == 'back':
        print(q[-1] if len(q) else -1)
    elif comm == 'size':
        print(len(q))
    elif comm == 'pop':
        print(q.popleft() if len(q) else -1)
    elif comm == 'empty':
        print(1 if not len(q) else 0)
