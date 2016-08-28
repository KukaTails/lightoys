class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        len_word1, len_word2 = len(word1), len(word2)
        dp = [[0 for i in range(len_word2+1)] for i in range(len_word1+1)]

        for i in range(len_word1+1):
            dp[i][0] = i
        for j in range(len_word2+1):
            dp[0][j] = j

        for i in range(1, len_word1+1):
            for j in range(1, len_word2+1):
                min_step = min(dp[i-1][j], dp[i][j-1]) + 1
                if word1[i-1] == word2[j-1]:
                    min_step = min(min_step, dp[i-1][j-1])
                else:
                    min_step = min(min_step, dp[i-1][j-1] + 1)
                dp[i][j] = min_step
        return dp[len_word1][len_word2]

# testing
test_cases = [['',''], ['a','b'], ['a', ''], ['', 'a'], ['a', 'a']]
for test_case in test_cases:
    print(Solution().minDistance(test_case[0], test_case[1]))