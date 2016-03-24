class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        return "" + self.convertToTitle((n - 1) / 26) + chr(ord('A') + (n - 1) % 26) if n > 0 else ""
