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
                    dp[i][j] = int(matrix[i][j])
                else:
                    if int(matrix[i][j]) == 1:
                        dp[i][j] = min([dp[i-1][j], dp[i][j-1], dp[i-1][j-1]]) + 1
                    else:
                        dp[i][j] = 0
        max_val = 0
        for i in range(rows):
            for j in range(columns):
                max_val = max([max_val, dp[i][j]])
        return max_val ** 2

# testing
test_cases = [["10"], ["10100","10111","11111","10010"], ["101101","111111","011011","111010","011111","110111"]]

for case in test_cases:
    print(Solution().maximalSquare(case))