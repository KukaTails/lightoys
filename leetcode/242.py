class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hash_s = {ch: 0 for ch in range(ord('a'), ord('z') + 1)}
        hash_t = {ch: 0 for ch in range(ord('a'), ord('z') + 1)}
        for ch in s:
            hash_s[ord(ch)] += 1
        for ch in t:
            hash_t[ord(ch)] += 1
        for i in range(ord('a'), ord('z') + 1):
            if hash_s[i] != hash_t[i]:
                return False
        return True