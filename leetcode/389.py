class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        hash_table = {}
        for ch in s:
            if ch in hash_table.keys():
                hash_table[ch] += 1
            else:
                hash_table[ch] = 1
        for ch in t:
            if ch not in hash_table.keys() or hash_table[ch] == 0:
                return ch
            else:
                hash_table[ch] -= 1


# testing
test_cases = [["abcd", "abcde"], ["a", "ba"], ["aaa", "abaa"], ["aaa", "aaaa"]]
for case in test_cases:
    print(Solution().findTheDifference(case[0], case[1]))