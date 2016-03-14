class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        self.n = len(obstacleGrid)
        self.m = len(obstacleGrid[0])
        self.grid = obstacleGrid
        self.dp = [[0 for i in xrange(self.m)] for i in xrange(self.n)]
        return self.findDp(0, 0)

    def findDp(self, n, m):
        if (n >= self.n or m >= self.m) or (self.grid[n][m] != 0):
            return 0
        if self.dp[n][m] != 0:
            return self.dp[n][m]
        if n == self.n - 1 and m == self.m - 1:
            self.dp[n][m] = 1
            return self.dp[n][m]
        self.dp[n][m] = self.findDp(n + 1, m) + self.findDp(n, m + 1)
        return self.dp[n][m]