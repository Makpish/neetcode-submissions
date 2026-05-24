class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1]*m
        for i in range(n-1):
            for j in range(m):
                if j>0:
                    dp[j] += dp[j-1]
        return dp[-1]
        