class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        seq = []
        while x != 0:
            seq.append(x % 10)
            x //= 10
        size = len(seq)
        i = 0
        j = size - 1
        while i <= j:
            if (seq[i] != seq[j]):
                return False
            else:
                i += 1
                j -= 1
        return True