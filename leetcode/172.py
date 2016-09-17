class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 0: return -1
        count = 0
        val = 5
        while val <= n:
            count += n // val
            val *= 5
        return count