class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        if (len(jobDifficulty) < d):
            return -1

        # 'i+1' 일 동안 첫 'j' 개의 작업을 완료하는 데 필요한 최소 난이도
        dp = [[0] * len(jobDifficulty) for _ in range(d)]
        dp[0][0] = jobDifficulty[0]
        for i in range(1, len(jobDifficulty)):
            dp[0][i] = max(dp[0][i - 1], jobDifficulty[i])

        for day in range(1, d):
            for i in range(day, len(jobDifficulty)):
                local = jobDifficulty[i]
                dp[day][i] = float('inf')
                for j in range(i, day - 1, -1):
                    local = max(local, jobDifficulty[j])
                    dp[day][i] = min(dp[day][i], dp[day - 1][j - 1] + local)

        return dp[-1][-1]
