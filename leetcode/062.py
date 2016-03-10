class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        MAX_N = 100 + 10
        dp = [[0] * MAX_N for i in range(MAX_N)]
        return self.findDp(0, 0, m, n, dp) + 1

    def findDp(self, i, j, m, n, dp):
        if i >= m or j >= n:
            return 0
        if dp[i][j] != 0:
            return dp[i][j]
        if i == m - 1 and j == n - 1:
            return dp[i][j]
        if i < m - 1 and j < n - 1:
            dp[i][j] = self.findDp(i + 1, j, m, n, dp) \
                       + self.findDp(i, j + 1, m, n, dp) + 1
        elif i < m - 1:
            dp[i][j] = self.findDp(i + 1, j, m, n, dp)
        else:
            dp[i][j] = self.findDp(i, j + 1, m, n, dp)
        return dp[i][j]
