class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        seq = [None] * 32
        for i in range(32):
            seq[i] = n & 0x1
            n >>= 1
        ans = 0
        for x in seq:
            ans = ans * 2 + x
        return ans