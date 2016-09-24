class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        length = len(matrix)
        for i in range(length):
            for j in range(i+1, length):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(length):
            self.reverse(matrix[i])

    @staticmethod
    def reverse(ls):
        i, j = 0, len(ls)-1
        while i < j:
            ls[i], ls[j] = ls[j], ls[i]
            i += 1
            j -= 1