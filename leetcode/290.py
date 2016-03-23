class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        strings = str.split()
        hashtable, charset = {}, set()
        if len(pattern) != len(strings): return False
        for i, ch in enumerate(pattern):
            string = hashtable.get(ch)
            if not string:
                if strings[i] in hashtable.values():
                    return False
                hashtable[ch] = strings[i]
            else:
                if string != strings[i]:
                    return False
        return True
