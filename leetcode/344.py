class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None: return ""
        word = [ch for ch in s]
        i, j = 0, len(word) - 1
        while i < j:
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        return "".join(word)

# testing
test_cases = [None, "", "a", "ab", "abc"]
for test_case in test_cases:
    print(Solution().reverseString(test_case))