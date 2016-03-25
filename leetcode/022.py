class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.ans, self.n = [], n
        self.helper("", 0, 0)
        return self.ans

    def helper(self, buckets, left, right):
        if left == self.n and right == self.n:
            self.ans.append(buckets)
            return
        if left > right:  self.helper(buckets + ")", left, right + 1)
        if left < self.n: self.helper(buckets + "(", left + 1, right)
