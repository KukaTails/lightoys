class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        dp = [[0] * m for i in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if obstacleGrid[i][j] != 0:
                    dp[i][j] = 0; continue
                if i == n - 1 and j == m - 1:
                    dp[i][j] = 1
                if i < n - 1:
                    dp[i][j] += dp[i + 1][j]
                if j < m - 1:
                    dp[i][j] += dp[i][j + 1]
        return dp[0][0]

# The solution below can not be accepted for it use functions.
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