class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        import math
        if n <= 0:
            return False
        res = math.log(n, 3)
        return True if abs(res - round(res)) < 1e-10 else False