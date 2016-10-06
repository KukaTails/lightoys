class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        is_not_negative = True if num >= 0 else False
        if not is_not_negative:
            num += 2 ** 31
            hex_value = self.convert_positive(num)
            hex_value = '0' * (8-len(hex_value)) + hex_value
            hex_value = Solution.get_digit(int(hex_value[0])+8) + hex_value[1:]
            return hex_value
        else:
            return self.convert_positive(num)

    @staticmethod
    def convert_positive(value):
        stack = [] if value != 0 else [0]
        while value:
            stack.append(value % 16)
            value //= 16
        hex_value = ""
        while stack:
            value = stack.pop()
            digit = Solution.get_digit(value)
            hex_value += digit
        return hex_value

    @staticmethod
    def get_digit(value):
        assert 0 <= value <= 15
        if value >= 10:
            digit = chr(ord('a') + value - 10)
        else:
            digit = str(value)
        return digit

# testing
test_cases = [-2**31, -1, 0, 1, 2, 15, 16, 17, 255, 256, 257, 2**31-1]
for case in test_cases:
    print(case, Solution().toHex(case), "{0:x}".format(case))
