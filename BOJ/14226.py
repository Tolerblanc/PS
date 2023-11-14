import sys
from collections import deque
input = sys.stdin.readline

s = int(input())
dp = [1001] * 10001
board = [False] * 10001

dp[1] = 0
q = deque([(1, 0, 0)]) #place, cost, clipboard
while q:
    curr, cost, clipboard = q.popleft()
    if not board[curr]:
        q.append((curr, cost + 1, curr))
        board[curr] = True
    if clipboard != 0 and curr + clipboard < 10000:
        q.append((curr + clipboard, cost + 1, clipboard))
        dp[curr + clipboard] = min(cost + 1, dp[curr + clipboard])
    if curr - 1 >= 2:
        q.append((curr - 1, cost + 1, clipboard))
        dp[curr - 1] = min(cost + 1, dp[curr - 1])
    if dp[s] != 1001:
        break
print(dp[s])