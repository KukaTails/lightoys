class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        len_i, len_j = len(matrix), len(matrix[0])
        first_row, first_column = False, False
        for i in range(len_i):
            if matrix[i][0] == 0:
                first_column = True; break
        for j in range(len_j):
            if matrix[0][j] == 0:
                first_row = True; break

        for i in range(1, len_i):
            for j in range(len_j):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0
        for i in range(1, len_i):
            if matrix[i][0] == 0:
                for j in range(len_j):
                    matrix[i][j] = 0
        for j in range(1, len_j):
            if matrix[0][j] == 0:
                for i in range(len_i):
                    matrix[i][j] = 0
        if first_column:
            for i in range(len_i):
                matrix[i][0] = 0
        if first_row:
            for j in range(len_j):
                matrix[0][j] = 0
