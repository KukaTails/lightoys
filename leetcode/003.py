class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        size = len(s)
        i = j = max_len = 0
        chars_set = set()

        while i < size and j < size:
            if i == j:
                chars_set.add(s[j])
                j += 1
            elif s[j] in chars_set:
                while s[i] != s[j]:
                    chars_set.remove(s[i])
                    i += 1
                chars_set.remove(s[i])
                i += 1
            else:
                chars_set.add(s[j])
                j += 1
            if j - i > max_len:
                max_len = j - i

        return max_len