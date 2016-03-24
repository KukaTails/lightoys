class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        ans = ["" for i in range(numRows)]
        for i in range(len(s)):
            k = i % (2 * numRows - 2) if numRows != 1 else 0
            if k >= numRows:
                k = 2 * numRows - 2 - k
            ans[k] += s[i]
        return reduce(lambda x, y: x + y, ans, "")
