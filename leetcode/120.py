class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        len_tri = len(triangle)
        dp = [[0] * len_tri for i in range(len_tri)]
        for i in range(len_tri):
            dp[len_tri - 1][i] = triangle[len_tri - 1][i]
        for i in range(len_tri - 2, -1, -1):
            for j in range(i + 1):
                dp[i][j] = min(dp[i+1][j], dp[i+1][j+1]) + triangle[i][j]
        return dp[0][0]
