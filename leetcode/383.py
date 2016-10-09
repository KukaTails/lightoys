class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hash_table = {}
        for letter in magazine:
            if letter in hash_table.keys():
                hash_table[letter] += 1
            else:
                hash_table[letter] = 1
        for letter in ransomNote:
            if letter not in hash_table.keys():
                return False
            elif hash_table[letter] == 0:
                return False
            else:
                hash_table[letter] -= 1
        return True
