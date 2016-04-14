class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        hashtable = {}
        for i in range(len(s) - 10 + 1):
            substr = s[i : i+10]
            if not hashtable.get(substr):
                hashtable[substr] = 1
            else:
                hashtable[substr] += 1
        ans = []
        for key, val in hashtable.items():
            if val > 1:
                ans.append(key)
        return ans