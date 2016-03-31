class Solution(object):
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.count = 0
        self.pos = [0] * n
        self.helper(0)
        return self.count

    def helper(self, row):
        import copy
        if row == self.n:
            self.count += 1
        else:
            for col in range(self.n):
                if self.is_safe(row, col):
                    self.pos[row] = col
                    self.helper(row + 1)

    def is_safe(self, row, col):
        for i in range(row):
            if abs(self.pos[i] - col) == abs(i - row) or self.pos[i] == col:
                return False
        return True