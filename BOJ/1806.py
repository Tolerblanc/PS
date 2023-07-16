import sys

input = sys.stdin.readline

n, s = map(int, input().split())
series = list(map(int, input().split()))
dp = []
suffix = 0
for num in series:
    suffix += num
    dp.append(suffix)

p1 = 0
p2 = 0
length = 100001
while p1 < n and p2 < n and p1 <= p2:
    suffix = dp[p2] - dp[p1] + series[p1]
    if suffix >= s:
        length = min(length, p2 - p1 + 1)
        p1 += 1
    else:
        p2 += 1
        
if length == 100001:
    print(0)
else:
    print(length)