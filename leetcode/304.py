class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix: return
        len_i = len(matrix)
        len_j = len(matrix[0])
        self.dp = [[0] * (len_j + 1) for i in range(len_i + 1)]
        for i in range(len_i + 1):
            for j in range(len_j + 1):
                if i == 0 or j == 0:
                    self.dp[i][j] = 0
                elif i == 1:
                    self.dp[i][j] = matrix[i-1][j-1] + (self.dp[i][j-1] if j != 1 else 0)
                else:
                    self.dp[i][j] = self.dp[i-1][j] + matrix[i-1][j-1] +\
                                    (self.dp[i][j-1] - self.dp[i-1][j-1] if j != 1 else 0)

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.dp[row2 + 1][col2 + 1] - self.dp[row1][col2 + 1] - self.dp[row2 + 1][col1] + self.dp[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# numMatrix = NumMatrix(matrix)
# numMatrix.sumRegion(0, 1, 2, 3)
# numMatrix.sumRegion(1, 2, 3, 4)
