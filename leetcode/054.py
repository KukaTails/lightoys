class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == None or len(matrix) == 0:
            return []
        start, self.matrix, self.ans = 0, matrix, []
        self.columns, self.rows = len(matrix[0]), len(matrix)
        while start * 2 < self.columns and start * 2 < self.rows:
            self.print_matrix_in_circle(start)
            start += 1
        return self.ans

    def print_matrix_in_circle(self, start):
        end_x = self.columns - 1 - start
        end_y = self.rows - 1 - start

        for i in range(start, end_x + 1):
            self.ans.append(self.matrix[start][i])
        if start < end_y:
            for i in range(start + 1, end_y + 1):
                self.ans.append(self.matrix[i][end_x])
        if start < end_x and start < end_y:
            for i in range(end_x - 1, start - 1, -1):
                self.ans.append(self.matrix[end_y][i])
        if start < end_x and start < end_y - 1:
            for i in range(end_y - 1, start, -1):
                self.ans.append(self.matrix[i][start])