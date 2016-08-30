class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        hash_table = {}
        for ch in s:
            if ch in hash_table.keys():
                hash_table[ch] += 1
            else:
                hash_table[ch] = 1
        for i, ch in enumerate(s):
            if hash_table[ch] == 1:
                return i
        return -1