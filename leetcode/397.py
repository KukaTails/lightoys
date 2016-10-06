class Solution(object):
    def integerReplacement(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.hashtable = {}
        return self.helper(n)

    def helper(self, n):
        if n == 1:
            return 0
        if n in self.hashtable.keys():
            return self.hashtable[n]
        if n % 2 == 0:
            res = 1 + self.helper(n // 2)
        else:
            res = 1 + min([self.helper(n + 1), self.helper(n - 1)])
        self.hashtable[n] = res
        return res