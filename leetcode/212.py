class TrieNode(object):
    def __init__(self, val):
        """
        Initialize your data structure here.
        """
        self.val = val
        self.is_end = False
        self.next = [None] * 32


class Trie(object):
    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                node.next[index] = TrieNode(ch)
            node = node.next[index]
        node.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for ch in word:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for ch in prefix:
            index = ord(ch) - ord('a')
            if not node.next[index]:
                return False
            node = node.next[index]
        return True

class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.ans, self.board, self.trie = [], board, self.build_trie(words)
        self.rows, self.column = len(board), len(board[0])
        self.visited = [[0] * self.column for i in range(self.rows)]
        for i in range(len(board)):
            for j in range(len(board[i])):
                self.visited[i][j] = True
                self.solve(i, j, board[i][j])
                self.visited[i][j] = False
        return list(sorted(set(self.ans)))


    def build_trie(self, words):
        trie = Trie()
        for word in words:
            trie.insert(word)
        return trie

    def pos_valid(self, i, j):
        if i < 0 or i >= self.rows or j < 0 or j >= self.column:
            return False
        else:
            return True

    def solve(self, i, j, word):
        if not self.pos_valid(i, j):
            return
        if not self.trie.startsWith(word):
            return
        if self.trie.search(word):
            self.ans.append(word)
        directions = ([-1, 0], [1, 0], [0, -1], [0, 1])
        for dire in directions:
            new_i, new_j = i + dire[0], j + dire[1]
            if not self.pos_valid(new_i, new_j) or self.visited[new_i][new_j]:
                continue
            self.visited[new_i][new_j] = True
            self.solve(new_i, new_j, word + self.board[new_i][new_j])
            self.visited[new_i][new_j] = False

# testing
test_cases = [(["aa"], ["aaa"]), (["oaan","etae","ihkr","iflv"], ["oath","pea","eat","rain"])]
for case in test_cases:
    print(Solution().findWords(case[0], case[1]))