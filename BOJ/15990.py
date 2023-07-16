import sys

input = sys.stdin.readline

n = int(input())
lst = []
size = 0
for _ in range(n):
    i = int(input())
    lst.append(i)
    if size < i:
        size = i
    
dp = [[0,0,0] for _ in range(size + 1)] #dp table (1end, 2end, 3end)
dp[1] = [1,0,0]
dp[2] = [0,1,0]
dp[3] = [1,1,1]

for i in range(4, size + 1):
    dp[i][0] = (dp[i-1][1] + dp[i-1][2]) % 1000000009
    dp[i][1] = (dp[i-2][0] + dp[i-2][2]) % 1000000009
    dp[i][2] = (dp[i-3][0] + dp[i-3][1]) % 1000000009

for l in lst:
    print(sum(dp[l]) % 1000000009)