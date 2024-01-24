def solution(n):
    dp = [1, 1, 2, 5]
    for i in range(4, n + 1):
        curr = 0
        for j in range(i):
            curr += dp[j] * dp[i - j]
        dp.append(curr)
    return dp
