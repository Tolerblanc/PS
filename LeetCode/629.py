class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (k + 1)
        dp[0] = 1

        for i in range(n):
            temp, number = [], 0
            for j in range(k + 1):
                number += dp[j]
                if j-i >= 1:
                    number -= dp[j-i-1]
                number %= MOD
                temp.append(number)
            dp = temp
        return dp[k]
