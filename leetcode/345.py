class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        word = [ch for ch in s]
        i, j = 0, len(word) - 1
        while i < j:
            while i < len(word) and word[i].lower() not in VOWELS: i += 1
            while j >= 0 and word[j].lower() not in VOWELS: j -= 1
            if i >= j: break
            word[i], word[j] = word[j], word[i]
            i += 1
            j -= 1
        return "".join(word)

# testing
test_cases = ["", "b", "abcdfg", "e", "efo", "abcd", "aA"]
for test_case in test_cases:
    print(Solution().reverseVowels(test_case))