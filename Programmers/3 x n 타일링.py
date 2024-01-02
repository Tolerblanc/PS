def solution(n):
    INF = 1_000_000_007
    dp = [0] * 5001
    dp[0] = 1
    dp[2] = 3
    for i in range(4, n + 1, 2):
        dp[i] = (dp[i - 2] * 4 - dp[i - 4]) % INF 
    return dp[n]