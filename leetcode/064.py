class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        MAX_N = 300 + 10
        m = len(grid)
        n = len(grid[0])
        dp = [[0] * MAX_N for i in range(MAX_N)]
        return self.findDp(0, 0, m, n, dp, grid)

    def findDp(self, i, j, m, n, dp, grid):
        import sys
        if i >= m or j >= n:
            return sys.maxint
        if dp[i][j] != 0:
            return dp[i][j]
        if i == m - 1 and j == n - 1:
            dp[i][j] = grid[i][j]
            return dp[i][j]
        min_num = min(self.findDp(i + 1, j, m, n, dp, grid),
                      self.findDp(i, j + 1, m, n, dp, grid))
        dp[i][j] = min_num + grid[i][j]
        return dp[i][j]
