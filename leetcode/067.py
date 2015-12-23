class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        len_a = len(a)
        len_b = len(b)
        max_size = max(len_a, len_b)
        a = "0" * (max_size - len_a) + a
        b = "0" * (max_size - len_b) + b

        carry = 0
        result = ""
        index = max_size - 1
        while index >= 0:
            sum = carry + ord(a[index]) + ord(b[index])- 2 * ord('0')
            result += str(sum & 0x1)
            carry = sum // 2
            index -= 1
        if carry:
            result += str(carry)
        return result[::-1]