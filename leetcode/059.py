class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 0: return []
        self.i = 0; self.j = 0; self.k = 1
        matrix = [[0] * n for i in range(n)]
        matrix[self.i][self.j] = self.k
        self.k += 1
        direction = [self.goRight, self.goDown, self.goLeft, self.goUp]
        dire_i = 0
        while self.k <= n * n:
            action = direction[dire_i % 4]
            while action(n, matrix):
                pass
            dire_i = (dire_i + 1) % 4
        matrix[self.i][self.j] = self.k - 1
        return matrix

    def goRight(self, n, matrix):
        if self.j + 1 >= n or matrix[self.i][self.j + 1] != 0:
            return False
        matrix[self.i][self.j + 1] = self.k
        self.k += 1; self.j += 1
        return True

    def goDown(self, n, matrix):
        if self.i + 1 >= n or matrix[self.i + 1][self.j] != 0:
            return False
        matrix[self.i + 1][self.j] = self.k
        self.k += 1; self.i += 1
        return True

    def goLeft(self, n, matrix):
        if self.j - 1 < 0 or matrix[self.i][self.j - 1] != 0:
            return False
        matrix[self.i][self.j - 1] = self.k
        self.k += 1; self.j -= 1
        return True

    def goUp(self, n, matrix):
        if self.i - 1 < 0 or matrix[self.i - 1][self.j] != 0:
            return False
        matrix[self.i - 1][self.j] = self.k
        self.k += 1; self.i -= 1
        return True
