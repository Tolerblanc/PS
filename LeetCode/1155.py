class Solution:
	def numRollsToTarget(self, n: int, k: int, target: int) -> int:
		MOD = 10**9 + 7
		dp = [[0] * 1001 for _ in range(31)]
		for i in range(1, k + 1):
		dp[1][i] = 1

		for i in range(2, n + 1):
			for j in range(i, i * k + 1):
				for l in range(1, k + 1):
					if j - l < 1:
						break
					dp[i][j] += dp[i - 1][j - l]
				dp[i][j] %= MOD
		return dp[n][target]