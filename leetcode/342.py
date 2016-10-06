class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return num > 0 and (num & (num-1) == 0) and (num & 0x555555555 == num)

# testing
test_cases = [0, 1, 2, 4, 8, 16, 32]
result = [False, True, False, True, False, True, False]
for i, test_case in enumerate(test_cases):
    assert Solution().isPowerOfFour(test_case) == result[i]