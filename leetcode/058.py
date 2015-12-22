class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        in_word = False
        len = 0
        for ch in s:
            if not in_word and ch != ' ':
                in_word = True
                len = 1
            elif in_word:
                if ch != ' ':
                    len += 1
                else:
                    in_word = False
        return len
