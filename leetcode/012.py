class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        factors = (1000, 900, 500, 400, 100,
                   90, 50, 40, 10, 9, 5, 4, 1)
        strs = ("M", "CM", "D", "CD", "C", "XC",
                "L", "XL", "X", "IX","V", "IV", "I")

        roman = ""
        for i, factor in enumerate(factors):
            if num <= 0: return roman
            k = num / factor
            num -= factor * k
            roman += k * strs[i]
        return roman