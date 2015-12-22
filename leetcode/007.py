class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        is_positive = True if x >= 0 else False
        val = abs(x)
        seq = []
        while val != 0:
            seq.append(val % 10)
            val //= 10
        for digit in seq:
            val = val * 10 + digit
        if val > 2 ** 31 - 1:
            return 0
        val = val if is_positive else -val
        return val