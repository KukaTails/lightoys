class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        res, k = 0, 1
        while k <= n:
            r = n // k
            m = n % k
            res += (r + 8) // 10 * k + (m + 1 if r % 10 == 1 else 0)
            k *= 10
        return res