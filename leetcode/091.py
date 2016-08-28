class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        len_s = len(s)
        dp = [1] * (len_s + 2)
        if not s: return 0
        has_error = False
        for i in range(len_s):
            index = i + 2
            if s[i] == '0':
                if i == 0 or not (1 <= int(s[i-1]) <= 2):
                    has_error = True
                dp[index] = dp[index-2]
            else:
                if i >= 1:
                    if s[i-1] == '0' or int(s[i-1:i+1]) >= 27:
                        dp[index] = dp[index-1]
                    else:
                        if i >= 2:
                            dp[index] = dp[index-1] + dp[index-2]
                        else:
                            dp[index] = dp[index-1] + 1
                else:
                    dp[index] = 1
        return dp[len_s+1] if not has_error else 0


# testing
test_cases = ['', '1029', '1238648392', '1', '11','111', "1111", '12', '20', '37', '137']
for test_case in test_cases:
    print(Solution().numDecodings(test_case))