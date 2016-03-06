class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        romans = ("I", "V", "X", "L", "C", "D", "M")
        nums = (1, 5, 10, 50, 100, 500, 1000)

        ans = i = 0
        len_str = len(s)
        while i < len_str:
            pos_now = romans.index(s[i])
            if i != len_str - 1:
                pos_next = romans.index(s[i + 1])
                if pos_now < pos_next:
                    ans += nums[pos_next] - nums[pos_now]
                    i += 1
                else:
                    ans += nums[pos_now]
            else:
                ans += nums[pos_now]
            i += 1
        return ans