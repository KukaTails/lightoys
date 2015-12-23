class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        flag = 0
        digits[0] += 1
        for i, digit in enumerate(digits):
            sum = digit + flag
            flag = sum // 10
            digits[i] = sum % 10
        if flag:
            digits.append(flag)
        digits.reverse()
        return digits