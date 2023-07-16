import sys

input = sys.stdin.readline
n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

dp = [1] * 12
dp[2] = 2 #11 2
dp[3] = 4 #111 12 21 3
# 4 = 1111 112 121 211 22 13 31
for i in range(4, 12):
    dp[i] = dp[i - 1] + dp[i - 2] + dp [i - 3]

for l in lst:
    print(dp[l])