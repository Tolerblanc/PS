import sys
from collections import deque
input = sys.stdin.readline

dp = [1000001] * 1000001
a, k = map(int, input().split())
dp[a] = 0
q = deque([(a, 0)])
while dp[k] == 1000001:
    qq = deque()
    while q:
        prev, cnt = q.popleft()
        if prev * 2 <= 1000000 and dp[prev * 2] > cnt + 1:
            dp[prev * 2] = cnt + 1
            qq.append((prev * 2, cnt + 1))
        if prev < 1000000 and dp[prev + 1] > cnt + 1:
            dp[prev + 1] = cnt + 1
            qq.append((prev + 1, cnt + 1))
    q = qq
print(dp[k])
