class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        self.visited = [False] * (2 ** n)
        self.ans, self.n, self.visited[0] = [0], n, True
        self.helper(0)
        return self.ans

    def helper(self, value):
        for i in range(self.n):
            tmp = value ^ (1 << i)
            if not self.visited[tmp]:
                self.ans.append(tmp)
                self.visited[tmp] = True
                self.helper(tmp)
