import sys
from bisect import bisect_left
input = sys.stdin.readline

n = int(input().strip())
lst = list(map(int, input().split()))
dp = [0]
for l in lst:
    dest = bisect_left(dp, l)
    if dest == len(dp) and dp[-1] < l:
        dp.append(l)
    else:
        dp[dest] = l

print(len(dp) - 1)
