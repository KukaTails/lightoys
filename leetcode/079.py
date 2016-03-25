class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board: return False
        self.len_i, self.len_j, self.len_word = len(board), len(board[0]), len(word)
        self.visited, self.board = [[False] * self.len_j for i in range(self.len_i)], board
        self.directions, self.word = [[-1, 0], [1, 0], [0, -1], [0, 1]], word
        for i in range(self.len_i):
            for j in range(self.len_j):
                if self.helper(0, i, j):
                    return True
        return False

    def helper(self, pos, i, j):
        if pos == self.len_word: return True
        if (not 0 <= i < self.len_i) or (not 0 <= j < self.len_j) or\
                self.visited[i][j] or self.board[i][j] != self.word[pos]:
            return False
        self.visited[i][j] = True
        for move in self.directions:
            if self.helper(pos + 1, i + move[0], j + move[1]):
                return True
        self.visited[i][j] = False
        return False
