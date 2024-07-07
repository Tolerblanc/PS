from collections import deque
import sys
input = sys.stdin.readline

deq = deque()
for _ in range(int(input())):
    comm, *arg = input().split()
    if comm == "push_back":
        deq.append(int(arg[0]))
    elif comm == "push_front":
        deq.appendleft(int(arg[0]))
    elif comm == "pop_front":
        print(deq.popleft() if deq else -1)
    elif comm == "pop_back":
        print(deq.pop() if deq else -1)
    elif comm == "size":
        print(len(deq))
    elif comm == "empty":
        print(0 if deq else 1)
    elif comm == "front":
        print(deq[0] if deq else -1)
    elif comm == "back":
        print(deq[-1] if deq else -1)
