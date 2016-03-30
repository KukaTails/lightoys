class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        self.p, self.s = p, s
        len_s, len_p = len(s), len(p)
        dp = [[False] * len_p for i in range(len_s)]
        for i in len_p:
            for j in len_s:
                if i == 0 and j == 0:
                    dp[i][j] = True if


/** so difficulut **/