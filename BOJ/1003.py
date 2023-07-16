import sys

input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

dp = [[1,0] for _ in range(41)]
dp[0] = [1,0]
dp[1] = [0,1]
#2 => fibo(1) + fibo(0) = dp[0] + dp[1]
#3 => fibo(2) + fibo(1) = dp[1] + dp[2]

for i in range(2,41):
    dp[i][0] = dp[i - 1][0] + dp[i - 2][0]
    dp[i][1] = dp[i - 1][1] + dp[i - 2][1]

for l in lst:
    print(dp[l][0], end = ' ')
    print(dp[l][1])