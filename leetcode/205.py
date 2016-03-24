class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = {}
        for i in range(len(s)):
            value = table.get(s[i])
            if not value:
                if t[i] in table.values():
                    return False
                table[s[i]] = t[i]
            else:
                if value != t[i]:
                    return False
        return True
