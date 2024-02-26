class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        dp = [0 for _ in range(len(s))]
        if s[-1] != '0':
            dp[-1] = 1
        if len(s) > 1 and s[-2] != '0':
            dp[-2] = dp[-1]
            if 1 <= int(s[-2:]) <= 26:
                dp[-2] += 1
        for i in range(len(s)-3, -1, -1):
            if s[i] == '0':
                continue
            dp[i] += dp[i + 1]
            if 1 <= int(s[i:i+2]) <= 26:
                dp[i] += dp[i + 2]
        return dp[0]
