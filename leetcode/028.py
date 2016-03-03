class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) + 1):
            for j in range(len(haystack) - i + 1):
                if j == len(needle): return i
                if i + j == len(haystack): return -1
                if haystack[i + j] != needle[j]: break