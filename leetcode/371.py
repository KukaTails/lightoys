class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        while a != 0 and b != 0:
            carry = (a & b) << 1
            tmp = a ^ b
            a, b = carry, tmp
        return b if a == 0 else a

# testing
test_case = [[3, 1]]
for case in test_case:
    print(Solution().getSum(case[0], case[1]))