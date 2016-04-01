class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = [0] * len_s
        has_error = False
        for i in range(len_s):
            if i == 0 and not 1 <= int(s[i]) <= 26:
                has_error = True
            if 1 <= int(s[i]) <= 26 or i >= 1:
                dp[i] = dp[i-1] if i >= 1 else 1
            else:
                dp[i] = dp[i-2] if i >= 1 else 0
            if i - 1 >= 0 and 1 <= int(s[i-1:i+1]) <= 26 and 1 <= int(s[i]) <= 26 and 1 <= int(s[i-1]) <= 26:
                if (i + 1 < len_s and 1 <= int(s[i+1]) <= 26) or i + 1 == len_s:
                    if i - 1 == 0:
                        dp[i] = 2
                    else:
                        dp[i] = max(dp[i-1], dp[i-2] + 1)
            if i >= 1 and not (1 <= int(s[i-1:i+1]) <= 26 or 1 <= int(s[i]) <= 26 or 1 <= int(s[i-1]) <= 26):
                has_error = True
        print(dp)
        return dp[len_s - 1] if len_s != 0 and not has_error else 0


print(Solution().numDecodings("111"))