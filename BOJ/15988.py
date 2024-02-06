import sys
input = sys.stdin.readline
MOD = 1_000_000_009

dp = [0, 1, 2, 4]
for i in range(1000001):
    dp.append((dp[-1] + dp[-2] + dp[-3]) % MOD)

for _ in range(int(input())):
    print(dp[int(input())])
