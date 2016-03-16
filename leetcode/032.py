class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = [0] * (len_s + 1)
        for i in range(1, len_s):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = 2 + (dp[i-2] if i != 1 else 0)
                elif (i - dp[i-1] - 1) >= 0 and s[i-dp[i-1]-1] == '(':
                    dp[i] = dp[i-1] + 2 + dp[i-dp[i-1]-2]
        return max(dp)
