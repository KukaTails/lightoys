class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if matrix == None or len(matrix) == 0: return 0
        rows, columns = len(matrix), len(matrix[0])
        dp = [[0] * columns for i in range(rows)]
        for i in range(rows):
            for j in range(columns):
                if i == 0 or j == 0:
                    dp[i][j] = matrix[i][j]
                else:
                    dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
        return dp[rows-1][columns-1]


# testing