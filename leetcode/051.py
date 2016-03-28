class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n, self.ans = n, []
        self.board = ['.' * n for i in range(n)]
        self.pos = [0] * n
        self.helper(0)
        return self.ans

    def helper(self, row):
        import copy
        if row == self.n:
            self.ans.append(copy.deepcopy(self.board))
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.pos[row] = col
                    self.board[row] = self.board[row][:col] + "Q" + self.board[row][col + 1:]
                    self.helper(row + 1)
                    self.board[row] = self.board[row][:col] + '.' + self.board[row][col + 1:]

    def is_safe(self, row, col):
        for i in range(row):
            if abs(self.pos[i] - col) == abs(i - row) or self.pos[i] == col:
                return False
        return True
