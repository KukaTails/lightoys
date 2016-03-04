class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strs = s.split()
        strs.reverse()
        return " ".join(strs)
