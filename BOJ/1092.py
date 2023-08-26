import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
crane = sorted(map(int, input().split()), reverse=True)
m = int(input())
box = deque(sorted(map(int, input().split()), reverse=True))


def solve():
    global m
    if box[0] > crane[0]:
        return -1
    count = 0
    while box:
        crane_cnt = 0
        count += 1
        for i in range(m):
            b = box.popleft()
            if crane_cnt < n:
                if crane[crane_cnt] >= b:
                    m -= 1
                    crane_cnt += 1
                else:
                    box.append(b)
            else:
                box.append(b)
        if (count >= 10000):
            break
    return count


print(solve())
